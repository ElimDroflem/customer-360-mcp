# Customer 360 MCP — Build Runbook

A terse step-by-step recipe for building a custom MCP server that stitches multiple real backends (Stripe + Supabase) into a single tool exposed to Claude Desktop. Use this to replicate the build on a new machine or as a template for similar MCPs.

Stack: Python 3.10+, Anthropic MCP SDK, Stripe SDK, Supabase SDK, python-dotenv, Claude Desktop, stdio transport (local only).

---

## Prerequisites

- Python 3.10+ installed (`python3 --version`)
- Stripe account with test mode access — secret key starts with `sk_test_`
- Supabase free-tier account (Postgres + dashboard)
- Claude Desktop installed and used at least once
- A terminal (zsh on macOS by default)

---

## Milestone 1 — Project setup, venv, dependencies, .env

**Critical: pick a project folder OUTSIDE iCloud-synced Documents.** iCloud Drive intercepts every file read to check sync status. A venv has thousands of files; Python startup and pip operations touch many of them; the cumulative latency makes the project feel broken (multi-second delays on trivial commands). Use `~/Projects/` or `~/Code/` instead of `~/Documents/`.

If you've already started in `~/Documents/` and need to migrate:

```bash
mkdir -p ~/Projects
mv ~/Documents/path/to/your-project ~/Projects/
cd ~/Projects/your-project
rm -rf .venv                      # venvs have hardcoded paths, must rebuild
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # the payoff for keeping requirements.txt current
```

### Project folder + virtual environment

```bash
cd ~/path/to/your/project-folder
python3 -m venv .venv
source .venv/bin/activate     # prompt should now show (.venv)
```

### macOS gotcha — Anaconda layering

If your prompt shows both `(.venv)` and `(base)`, Anaconda's auto-activate is silently adding seconds to every Python call. Disable it permanently:

```bash
conda config --set auto_activate_base false
conda deactivate              # for current session
```

After this, every new terminal session for the project just needs:

```bash
cd ~/path/to/project-folder
source .venv/bin/activate
```

### Install dependencies

```bash
pip install stripe python-dotenv
pip freeze > requirements.txt
```

Re-run `pip freeze > requirements.txt` after every new package install to keep the manifest current. Anyone reproducing the env runs `pip install -r requirements.txt`.

### .gitignore

```bash
printf ".venv\n.env\n" > .gitignore
```

Two non-negotiables: `.venv` (regenerable, machine-specific, huge) and `.env` (secrets). The `.env` line is the most important line you'll ever write in a `.gitignore`.

### Secrets via .env

```bash
nano .env
```

Add one line per secret, no quotes, no spaces around `=`:

```
STRIPE_SECRET_KEY=<YOUR_STRIPE_TEST_KEY>
```

Save: `Ctrl+X`, `Y`, `Enter`. Verify with `cat .env`.

Avoid `echo "..." > .env` — that puts the secret in your shell history file.

---

## Architectural concepts to be able to explain in interviews

- **Virtual environments**: per-project isolation of Python dependencies. The local-laptop equivalent of a Docker container. Same isolation principle, different failure boundary. Production uses containers; local uses venvs.

- **Secrets handling — the spectrum**:
  - `.env` on disk (this build): bare metal. Fine for solo dev. Threat model = laptop compromise.
  - Platform env vars (Vercel/Heroku/Netlify): solves distribution + storage. Still static-config-injected.
  - Secrets manager (AWS Secrets Manager, HashiCorp Vault): runtime fetch with per-call audit log, IAM-scoped access, instant revocation. The fintech production answer.
  - One-line interview compression: "I used `.env` for local dev; the same code reads from `os.environ` at runtime, so swapping in a secrets manager is a config change, not a code change."

- **`requirements.txt`**: the reproducibility manifest. In production, the Docker build runs `pip install -r requirements.txt` instead of a developer typing pip from memory.

- **SDK over raw HTTP**: build-vs-buy decision. Stripe's SDK handles auth, retries, typed error classes, API-version pinning. Maintaining your own HTTP client for a stable third-party API is wasted engineering effort. The wrong default is "I'll just use `requests`" — that's how teams burn weeks reinventing what already exists.

---

*Sections to be added as we hit later milestones: Stripe seed data, Supabase tables, MCP server scaffold, wiring backends, scoping/audit/error handling, Claude Desktop integration.*
