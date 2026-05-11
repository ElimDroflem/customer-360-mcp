"""
Seed Supabase with mock comms history and risk flags,
linked to the Stripe customers we created in seed_stripe.py.

Looks up Stripe customers by name at runtime — no hardcoded IDs.
Run once on a fresh database. Re-running creates duplicates.
"""

import os
import stripe
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SERVICE_ROLE_KEY"],
)

# Mock data per customer. Variety is deliberate:
# Alice has the disputed charge + matching risk flags.
# Ben's account is clean — no flags.
# Chris has a KYC flag, lower severity.
SEED_DATA = {
    "Alice Henderson": {
        "comms": [
            {"channel": "email", "subject": "Re: Travel charge query",
             "body": "Hi Alice, we've received your dispute on the British Airways charge. We'll be in touch within 5 working days while we investigate."},
            {"channel": "phone", "subject": "Inbound call — disputed transaction",
             "body": "Customer called to report unrecognised £450 charge. Confirmed travel was booked but cancelled. Advised to file dispute via banking app."},
            {"channel": "email", "subject": "Welcome to your business card",
             "body": "Hi Alice, welcome to Capital on Tap. Your card has been despatched and should arrive within 3 working days."},
        ],
        "flags": [
            {"flag_type": "active_dispute", "severity": "high",
             "notes": "Open dispute on £450 BA charge — under investigation."},
            {"flag_type": "manual_review_recommended", "severity": "medium",
             "notes": "Pattern flagged: high-value travel charge then dispute within 7 days."},
        ],
    },
    "Ben Roberts": {
        "comms": [
            {"channel": "chat", "subject": "Account upgrade query",
             "body": "Asked about upgrading to the higher rewards tier. Explained eligibility; said he'd think about it."},
            {"channel": "email", "subject": "Statement available",
             "body": "Your monthly statement for April 2026 is now available in the app."},
        ],
        "flags": [],
    },
    "Chris Yamamoto": {
        "comms": [
            {"channel": "in_app", "subject": "Limit increase requested",
             "body": "Customer requested credit limit increase from £5k to £15k via app. Routed to underwriting."},
        ],
        "flags": [
            {"flag_type": "kyc_review_pending", "severity": "low",
             "notes": "Periodic KYC refresh due — automated reminder sent."},
        ],
    },
}


def seed():
    print("Fetching Stripe customers...")
    customers = stripe.Customer.list(limit=100)
    name_to_id = {c.name: c.id for c in customers.data}
    print(f"Found {len(name_to_id)} customer(s) in Stripe.\n")

    total_comms = 0
    total_flags = 0

    for name, data in SEED_DATA.items():
        customer_id = name_to_id.get(name)
        if customer_id is None:
            print(f"Skipping {name} — not found in Stripe. Run seed_stripe.py first.")
            continue

        print(f"Seeding for {name} ({customer_id})")

        if data["comms"]:
            rows = [{**c, "stripe_customer_id": customer_id} for c in data["comms"]]
            supabase.table("comms_history").insert(rows).execute()
            print(f"  + {len(rows)} comms entries")
            total_comms += len(rows)

        if data["flags"]:
            rows = [{**f, "stripe_customer_id": customer_id} for f in data["flags"]]
            supabase.table("risk_flags").insert(rows).execute()
            print(f"  + {len(rows)} risk flags")
            total_flags += len(rows)
        else:
            print(f"  (no risk flags — clean account)")

        print()

    print(f"Done. {total_comms} comms entries, {total_flags} risk flags inserted.")


if __name__ == "__main__":
    seed()
