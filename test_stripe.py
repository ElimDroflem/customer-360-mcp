import os
import stripe
from dotenv import load_dotenv

# Load .env into the OS environment
load_dotenv()

# Hand the secret key to the Stripe SDK
stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

# Sanity check: list up to 5 customers (fresh test mode = empty)
customers = stripe.Customer.list(limit=5)

print(f"Stripe key works. Found {len(customers.data)} customer(s).")
for c in customers.data:
    print(f"  - {c.id}: {c.email}")
