"""
Seed Stripe test mode with customers, charges, and a dispute.

Run once on a fresh test account. To re-seed, clear test data first
via Stripe Dashboard: Developers → Test data → 'Delete all test data'.
"""

import os
import stripe
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

SEED_CUSTOMERS = [
    {
        "email": "alice@acmecorp.example",
        "name": "Alice Henderson",
        "metadata": {"business": "Acme Corp Ltd", "segment": "small_business"},
        "charges": [
            {"amount": 12500, "description": "Office supplies — Staples"},
            {"amount": 8200,  "description": "Software — GitHub"},
            {"amount": 45000, "description": "Travel — British Airways", "dispute": True},
        ],
    },
    {
        "email": "ben@retailco.example",
        "name": "Ben Roberts",
        "metadata": {"business": "Retail Co", "segment": "small_business"},
        "charges": [
            {"amount": 5400,  "description": "Stripe subscription"},
            {"amount": 18900, "description": "Marketing — Meta Ads"},
        ],
    },
    {
        "email": "chris@growthlab.example",
        "name": "Chris Yamamoto",
        "metadata": {"business": "Growth Lab Ltd", "segment": "scaleup"},
        "charges": [
            {"amount": 25000, "description": "Cloud — AWS"},
            {"amount": 9900,  "description": "SaaS — Notion"},
        ],
    },
]


def seed():
    print(f"Seeding {len(SEED_CUSTOMERS)} customers...\n")
    for c in SEED_CUSTOMERS:
        customer = stripe.Customer.create(
            email=c["email"],
            name=c["name"],
            source="tok_visa",
            metadata=c["metadata"],
        )
        print(f"Created customer {customer.id} — {customer.name}")

        for ch in c["charges"]:
            if ch.get("dispute"):
                dispute_card = stripe.Customer.create_source(
                    customer.id, source="tok_createDispute"
                )
                charge = stripe.Charge.create(
                    amount=ch["amount"], currency="gbp",
                    customer=customer.id, source=dispute_card.id,
                    description=ch["description"],
                )
                marker = "[DISPUTE]"
            else:
                charge = stripe.Charge.create(
                    amount=ch["amount"], currency="gbp",
                    customer=customer.id,
                    description=ch["description"],
                )
                marker = ""
            print(f"  £{ch['amount']/100:>7.2f}  {ch['description']:<40} {marker} {charge.id}")
        print()

    print("Done. Check the Stripe Dashboard to confirm.")


if __name__ == "__main__":
    seed()
