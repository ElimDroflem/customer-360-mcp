# Customer 360 MCP Server

A custom Model Context Protocol (MCP) server that stitches multiple real backends into a single purpose-built tool for AI agents, with role-based scoping and audit logging. Built as a demonstration of the architectural pattern fintechs use to expose customer data to AI safely.

The pitch in one line: **one purpose-built tool, multiple real backends stitched server-side, scoped output, audit-logged at the boundary you control.**

---

## What it does

Exposes one tool to Claude Desktop:

```python
get_customer_360(customer_id: str, agent_level: "junior" | "senior" = "junior") -> dict
```

When called, the tool fetches:

- Customer profile from **Stripe**
- Recent charges from **Stripe**
- Open disputes from **Stripe** (filtered to this customer's charges)
- Last 5 communications from **Supabase**
- Currently active risk flags from **Supabase**

…then returns a single structured response combining all five sources, with field-level redaction based on the calling agent's role.

A junior agent sees the customer's email redacted (`a***@acmecorp.example`) and risk flags without their `notes`. A senior agent sees the full record. Same tool, same customer, two different views — enforced at the server, not at the AI client.

---

## How it's wired

```
Claude Desktop  ──stdio──▶  server.py  ──HTTPS──▶  Stripe API
                                       ──HTTPS──▶  Supabase (Postgres)
```

- **Transport**: stdio. Claude Desktop launches `server.py` as a subprocess at startup. Local-only; nothing exposed to the internet.
- **Auth**: Stripe secret key + Supabase service-role key, loaded from `.env` at startup, never committed to version control.
- **Scoping**: `agent_level` parameter controls field-level redaction.
- **Errors**: every backend call wrapped in try/except, returns structured error responses rather than raw stack traces.
- **Audit**: every call appends a UTC-timestamped line to `audit.log`.

---

## Why a custom MCP — when off-the-shelf options exist

Off-the-shelf MCPs (Stripe's official MCP, GitHub's, etc.) are great when you want general AI access to a single platform's capabilities. A custom MCP earns its keep when any of these apply:

- **Scoping by role**. Different agents see different data. Junior support sees redacted fields; senior fraud sees the full record. Off-the-shelf MCPs can't do this.
- **Stitching**. Combine multiple backends into one coherent answer the AI doesn't have to reconcile in its own head.
- **Server-enforced rules**. Filter at the boundary you control, where the rules can't be talked around by clever prompting.
- **Audit logging**. Every call captured with caller, customer, role, and outcome — defensible to security review.

For this demo: Capital on Tap (or any regulated fintech) couldn't safely use Stripe's off-the-shelf MCP because it dumps everything regardless of who's asking. A custom MCP layers the company's actual access controls and stitches in their internal data systems alongside Stripe.

The interview-ready compression: **off-the-shelf MCPs expose too much and combine too little; custom MCPs are how you make AI access defensible in regulated environments.**

---

## Setup

```bash
git clone <repo-url>
cd customer-360-mcp

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Add Stripe + Supabase credentials to .env
cp .env.example .env
# then edit with your sk_test_... and Supabase URL + service-role key

# Seed test data into both backends
python seed_stripe.py
python seed_supabase.py

# Confirm function works directly
python test_real.py
```

Then register with Claude Desktop. Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "customer-360": {
      "command": "/absolute/path/to/.venv/bin/python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

Fully quit (`Cmd+Q`) and reopen Claude Desktop. The `customer-360` tool will appear in the connectors pane.

---

## Demo prompts

To reproduce the demo screenshots:

1. *"Look up customer cus_XXXX using my customer-360 tool."* — baseline call (default junior scope).
2. *"Now look up the same customer as a senior agent. What's different?"* — scoping in action; the server returns more fields.
3. *"Look up cus_DEFINITELYNOTREAL — what happens?"* — graceful error path; tool returns `{ "error": "customer_not_found", ... }` with no crash.
4. *"Look up cus_XXXX as a senior agent and summarise what's going on, including any actions I should take."* — the synthesis demo: Claude reads the stitched response, identifies the actionable item, and recommends next steps.

To prove scoping at the data layer (not just through Claude's narration), run `python test_real.py` — it prints the junior and senior JSON side by side. The redaction is at the server, not at the agent.

---

## What would change in production at a regulated fintech

This demo is deliberately scoped to be runnable on a laptop. The architectural pattern is what carries to production; the implementation details would change.

### Secrets management
- `.env` on disk → AWS Secrets Manager / HashiCorp Vault.
- Service-role key fetched at runtime via IAM role attached to the runtime.
- Per-call audit of secret access in addition to per-call audit of tool invocation.

### Transport
- stdio (laptop-only) → Streamable HTTP with mTLS.
- Server runs as a hardened service (Kubernetes pod, ECS task, etc.) — not on the user's machine.
- Multiple agent clients (Claude Desktop, internal copilots, customer-service AI) connect to the same shared server.

### Authentication and authorisation
- `agent_level` parameter trusted from the agent → derived from the agent's authenticated identity (LDAP / SSO group / SCIM-provisioned role).
- Per-customer scoping enforced via Postgres row-level security as defence in depth — even if the application layer is bypassed.
- Approval workflows or human-in-the-loop gates for high-risk actions.

### Observability
- Flat-file audit log → structured logs to Splunk / Datadog / SIEM.
- Distributed tracing across Stripe → MCP → agent for incident response.
- Metrics on call rate, latency, error rate, redaction events — broken down by `agent_level`.

### Resilience
- Plain `try/except` → per-error-type retry policies (network errors retry with backoff; `not_found` doesn't).
- Idempotency keys on any mutating Stripe calls.
- Circuit breakers on Stripe and Supabase calls.

### Data minimisation
- Currently scoping by stripping fields after fetch → production also scopes by query (don't even fetch data the agent shouldn't see).
- Field-level encryption at rest for fields that have to be stored but should rarely be displayed (full PAN, full SSN-equivalents, etc.).

### Seed-script idempotency
- Current seeds duplicate on re-run → production seeds use idempotency keys and check-and-skip patterns so they're safe to re-run as part of CI/CD.

---

## What this demonstrates

This MCP is built as a demo for AI Adoption / AI Operations roles at regulated companies. It's intended to demonstrate:

- Ability to ship a working MCP server end-to-end: Python, MCP SDK, Stripe, Supabase, Claude Desktop integration.
- Judgement on when custom MCPs earn their keep over off-the-shelf integrations.
- Multi-backend stitching with sensible API design.
- Awareness of the regulatory and operational layer: scoping, redaction, audit logging, secrets management.
- Articulation of what changes at production-regulated-environment scale (the section above is the actual interview content).

---

## File map

| File | Purpose |
| --- | --- |
| `server.py` | The MCP server. Defines `get_customer_360` and registers it with Claude Desktop via FastMCP. |
| `seed_stripe.py` | Creates 3 customers, 8 charges, 1 dispute in Stripe test mode. Run once. |
| `seed_supabase.py` | Creates 6 comms entries, 3 risk flags in Supabase, linked to the Stripe customer IDs. Run once. |
| `test_real.py` | Calls `get_customer_360` directly (bypassing Claude Desktop) to verify the function works and to prove the junior/senior scoping at the data layer. |
| `audit.log` | Append-only log of every tool invocation. Auto-created on first call. |
| `.env` | Secrets — Stripe key, Supabase URL, Supabase service-role key. Gitignored. |
| `.env.example` | Template showing required keys without values. Safe to commit. |
| `requirements.txt` | Pinned Python dependencies. |
| `BUILD-RUNBOOK.md` | Step-by-step build notes — useful as a recipe to replicate this on a new machine. |
