import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SERVICE_ROLE_KEY"],
)

# Cheapest possible call: read up to 1 row from each table.
# Empty result = success (tables exist, auth works, network works).
comms = supabase.table("comms_history").select("*").limit(1).execute()
flags = supabase.table("risk_flags").select("*").limit(1).execute()

print(f"Supabase connection works.")
print(f"  comms_history: {len(comms.data)} row(s)")
print(f"  risk_flags:    {len(flags.data)} row(s)")
