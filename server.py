"""
Customer 360 MCP server.

Exposes one tool to Claude Desktop: get_customer_360(customer_id, agent_level).
Stitches data from Stripe (payments) and Supabase (comms + risk flags)
into one structured response, with role-based scoping and audit logging.
"""

import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

import stripe
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from supabase import create_client

load_dotenv(Path(__file__).parent / ".env")

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SERVICE_ROLE_KEY"],
)

# Every tool call appends one line here.
# In production this would go to Splunk / Datadog / a SIEM, not a file.
AUDIT_LOG = Path(__file__).parent / "audit.log"


def audit(event: str, **fields) -> None:
    """Append a structured line to the audit log."""
    line = f"{datetime.now(timezone.utc).isoformat()} {event}"
    for k, v in fields.items():
        line += f" {k}={v}"
    with AUDIT_LOG.open("a") as f:
        f.write(line + "\n")


def redact_email(email: str | None) -> str | None:
    """Mask the local part of an email: alice@acmecorp.example -> a***@acmecorp.example."""
    if not email or "@" not in email:
        return email
    name, domain = email.split("@", 1)
    return f"{name[0]}***@{domain}"


mcp = FastMCP("customer-360")


@mcp.tool()
def get_customer_360(
    customer_id: str,
    agent_level: Literal["junior", "senior"] = "junior",
) -> dict:
    """
    Return a 360-degree view of a customer:
    profile, recent transactions, open disputes,
    recent comms history, and current risk flags.

    The agent_level parameter controls how much detail is returned.
    - "junior": email is redacted, risk flag notes are stripped.
    - "senior": full record including unredacted email and notes.

    Use this when the user asks about a specific customer
    and provides a Stripe customer ID (e.g. cus_ABC123).
    """
    audit("tool.called", customer_id=customer_id, agent_level=agent_level)

    # 1. Customer profile from Stripe
    try:
        customer = stripe.Customer.retrieve(customer_id)
    except stripe.error.InvalidRequestError:
        audit("tool.error", stage="customer_fetch", reason="not_found",
              customer_id=customer_id)
        return {
            "error": "customer_not_found",
            "message": f"No customer with ID {customer_id}",
            "customer_id": customer_id,
        }
    except Exception as e:
        audit("tool.error", stage="customer_fetch", reason=str(e))
        return {"error": "upstream_failure", "stage": "customer_fetch",
                "message": str(e)}

    raw_email = customer.email
    profile = {
        "id": customer.id,
        "name": customer.name,
        "email": raw_email if agent_level == "senior" else redact_email(raw_email),
        "created": customer.created,
        "metadata": customer.metadata.to_dict() if customer.metadata else {},
    }

    # 2 & 3. Charges and disputes from Stripe
    try:
        charges = stripe.Charge.list(customer=customer_id, limit=10)
        transactions = [
            {
                "id": ch.id,
                "amount_pence": ch.amount,
                "currency": ch.currency,
                "description": ch.description,
                "status": ch.status,
                "disputed": ch.disputed,
                "created": ch.created,
            }
            for ch in charges.data
        ]

        charge_ids = {t["id"] for t in transactions}
        all_disputes = stripe.Dispute.list(limit=20)
        disputes = [
            {
                "id": d.id,
                "charge": d.charge,
                "amount_pence": d.amount,
                "currency": d.currency,
                "reason": d.reason,
                "status": d.status,
                "created": d.created,
            }
            for d in all_disputes.data
            if d.charge in charge_ids
        ]
    except Exception as e:
        audit("tool.error", stage="stripe_charges_or_disputes", reason=str(e))
        return {"error": "upstream_failure", "stage": "stripe_charges_or_disputes",
                "message": str(e)}

    # 4 & 5. Comms and risk flags from Supabase
    try:
        comms = (
            supabase.table("comms_history")
            .select("*")
            .eq("stripe_customer_id", customer_id)
            .order("created_at", desc=True)
            .limit(5)
            .execute()
            .data
        )
        flags = (
            supabase.table("risk_flags")
            .select("*")
            .eq("stripe_customer_id", customer_id)
            .is_("resolved_at", "null")
            .order("created_at", desc=True)
            .execute()
            .data
        )
    except Exception as e:
        audit("tool.error", stage="supabase_fetch", reason=str(e))
        return {"error": "upstream_failure", "stage": "supabase_fetch",
                "message": str(e)}

    # Junior agents don't see risk flag notes
    if agent_level == "junior":
        for flag in flags:
            flag.pop("notes", None)

    audit("tool.success", customer_id=customer_id, agent_level=agent_level,
          transactions=len(transactions), disputes=len(disputes),
          comms=len(comms), flags=len(flags))

    return {
        "customer_id": customer_id,
        "agent_level": agent_level,
        "profile": profile,
        "transactions": transactions,
        "disputes": disputes,
        "comms": comms,
        "risk_flags": flags,
    }


if __name__ == "__main__":
    mcp.run()
