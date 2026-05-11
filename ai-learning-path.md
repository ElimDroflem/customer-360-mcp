# AI Adoption / AI Operations Learning Path — Curated for Corey

**Audience:** Mid-career UK operator interviewing for AI Adoption Lead at Capital on Tap and similar roles. Already comfortable with Claude Code, Cursor, Lovable, V0, Cowork. Goal: deepen understanding of how AI systems are designed, planned, and rolled out inside businesses, with a UK fintech bias.

**Curatorial bias:** Content from people who have actually shipped AI inside companies (operators, engineers, PMs) over content from generic AI commentators. 2024 onward only. Where I couldn't find substantive third-party reviews, I say so.

---

## 1. Structured Courses

### Tier 1 — Almost certainly worth your time

**Hamel Husain & Shreya Shankar — AI Evals for Engineers & PMs (Maven)**
- https://maven.com/parlance-labs/evals
- ~4 weeks, cohort-based, ~$2,000 (often discounted). #1 highest-grossing Maven course; over 2,000 alumni from OpenAI, Anthropic, and 500+ other companies.
- **What it teaches:** error analysis, synthetic data generation, LLM-as-judge, RAG debugging, CI/CD integration. The methodology used internally at the major labs.
- **Why it matters for an Adoption Lead:** evals are how you prove an AI initiative is working in production. If you can talk fluently about error analysis and LLM-as-judge in the Capital on Tap interview, you will sound like the most senior person in the room. This is the single most leveraged course on the list.
- **Caveat:** technical. Assumes you can read Python. If that's a wall, take Andrew Ng's Agentic AI first.

**Andrew Ng — Agentic AI (DeepLearning.AI)**
- https://www.deeplearning.ai/courses/agentic-ai
- 5 modules, self-paced, free to audit / ~$25/month for certificate.
- **What it teaches:** the four foundational agentic design patterns (Reflection, Tool Use, Planning, Multi-Agent Collaboration) in vendor-neutral Python.
- **Why it matters:** these four patterns are now the shared vocabulary. You will hear "reflection loop" and "planner-executor" in interviews; this course gives you the canonical mental model.
- **Caveat:** conceptual rather than project-heavy. Pair it with actually building something in Claude Code.

**Anthropic Academy (free)**
- https://www.anthropic.com/learn
- Four official free courses: Claude with the Anthropic API, Introduction to Agent Skills, Introduction to Model Context Protocol, Claude Code in Action.
- **Why it matters:** you are interviewing into a Claude-using world. The MCP course in particular is directly relevant — Capital on Tap and any modern AI team will be evaluating MCP architecture choices in 2026. Free, fast, official.

### Tier 2 — Worth it if you have the time/budget

**Reforge — AI Product Leadership / AI Strategy / AI Foundations**
- https://www.reforge.com/courses/ai-product-leadership
- ~$2,000. Designed for senior PMs, Directors, Heads of Product.
- **What it teaches:** how to reshape a PM/leader role with AI; aimed at strategy and team operating model changes, not technical execution.
- **Honest take:** the content is good but the pricing is steep relative to free alternatives. The real value is the network — meeting senior PMs from Stripe, Airbnb, Spotify in cohort. If networking matters for your next move, take it; otherwise skip and use the saved hours on building.

**AI Product Academy — AI PM Bootcamp (Maven, Marily Nika et al.)**
- https://maven.com/marily-nika/ai-pm-bootcamp
- Strong instructor signal (Marily Nika is AI PM at Google; Deb Liu was CEO of Ancestry).
- **What it teaches:** practical AI PM workflow, prototyping, mentorship to launch a real AI product.
- **Verdict:** good for someone less hands-on than Corey already is. If you're already shipping with Claude Code, the marginal value is lower.

**Section AI — AI Mini-MBA (Scott Galloway)**
- https://www.sectionai.com/
- Live cohort, business-school framing.
- **Honest take:** strong on storytelling and "frame this for executives" muscle; weaker on technical depth than the Maven options. Useful if your Capital on Tap interview includes a board-level pitch component. Skip if you want to build.

### Tier 3 — Mostly skip

- **IBM AI Product Manager Professional Certificate (Coursera)**, **Pragmatic Institute AI for PMs**, **Product School AI for PMs**: brand-name certificates that look fine on LinkedIn but the curriculum lags meaningfully behind what working practitioners are doing. Cert-shaped résumé padding, not real upskilling.
- **Generic "AI for Business" Coursera/edX tracks**: most are 2022–2023 vintage. Avoid.

---

## 2. Books (2024 onward only)

**Co-Intelligence — Ethan Mollick (2024)** — https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/
The single best "how to think about AI in a workplace" book. NYT bestseller, FT/Economist book of the year. Mollick runs Wharton's Generative AI Lab and tests this stuff on actual workers. Read this first. It's the book a Capital on Tap exec is most likely to have read.

**AI Engineering — Chip Huyen (O'Reilly, January 2025)** — https://www.oreilly.com/library/view/ai-engineering/9781098166298/
The most-read book on O'Reilly since release. Covers foundation models, evals, prompt vs. fine-tune vs. API choice, deployment, product alignment. Technical but readable. This is the reference text for "how AI systems are actually built." Don't read cover to cover — use it as a lookup when you encounter a concept you can't explain.

**The Enterprise AI Playbook — Stanford Digital Economy Lab (2026)** — https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf
Free PDF. 51 case studies of enterprise AI deployments where value was actually measured. Brynjolfsson is the senior name; the framework on human-in-the-loop oversight (65% of high performers vs. 23% of laggards) is the kind of stat that wins interviews.

**Evals for AI Engineers — Husain & Shankar (O'Reilly)** — https://www.oreilly.com/library/view/evals-for-ai/9798341660717/
Companion to the Maven course. If the cohort is too expensive, the book gets you 60–70% of the way there.

**All-In on AI — Davenport & Mittal (2023, but still cited)**
The "old" enterprise-AI canon. Slightly dated post-ChatGPT-5 but the organizational change-management chapters age well. Borrow, skim, don't buy.

**Skip:** anything titled "AI Strategy" published before mid-2023, anything by a generic management consultancy, and any book that promises a "12-step framework." The field moves too fast.

---

## 3. Newsletters & Substacks

**Tier 1 — read every issue:**

- **One Useful Thing — Ethan Mollick** — https://www.oneusefulthing.org/ — research-backed, practical, never hyped. 433k+ subscribers. The reference newsletter.
- **Simon Willison's Weblog** — https://simonwillison.net/ — daily TIL-style notes from a working engineer experimenting with every new model. Best signal-to-noise on what actually works in tools and code.
- **Latent Space — swyx & Alessio Fanelli** — https://www.latent.space/ — newsletter half of the podcast (see below). Covers what AI engineers are actually shipping. The trade publication of AI engineering.

**Tier 2 — skim weekly:**

- **Chain of Thought — Dan Shipper / Every** — https://every.to/chain-of-thought — essay-driven, strategic-operator angle. Every is also publishing operational case studies.
- **Stratechery — Ben Thompson** — https://stratechery.com/ — paid. Best on AI as competitive strategy at the Microsoft/Google/Anthropic level. Reads less useful for day-to-day execution but vital for understanding the platform dynamics shaping your tools.
- **Lenny's Newsletter — Lenny Rachitsky** — https://www.lennysnewsletter.com/ — biggest PM newsletter in the world. Recent AI series (vibe coding, AI agents for PMs, building eval systems with Hamel & Shreya) is genuinely good.
- **The Pragmatic Engineer — Gergely Orosz** — strong AI tooling coverage from a senior-engineer perspective.

**Skip-tier — overhyped:** The Rundown AI, Superhuman AI, TLDR AI. They pile up subscribers but optimize for headline volume, not insight. Fine if you want to feel current; useless for going deep.

---

## 4. Podcasts

- **Latent Space (swyx & Alessio)** — https://www.latent.space/podcast — the consensus pick for AI engineering. Weekly, ~75 min, interviews with senior engineers at OpenAI, Anthropic, Sierra, Databricks. The one to default to.
- **No Priors (Sarah Guo & Elad Gil)** — https://www.nopriors.com/ — investor-flavored, talks to founders and researchers. Good for keeping your strategic vocabulary current.
- **The AI Daily Brief (Nathaniel Whittemore)** — https://aidailybrief.beehiiv.com/ — daily, business/enterprise lens. Great for the commute. Best 15-minute-a-day option.
- **Lenny's Podcast** — https://www.lennysnewsletter.com/podcast — Lenny interviews PMs, founders, and recently a lot of AI operators (Hamel, Shreya, Simon Willison). The Mollick and Willison episodes are required listening.
- **Practical AI** — fine but lower signal density than the above. Optional.

---

## 5. YouTube / Video

- **AI Engineer (@aiDotEngineer)** — https://www.youtube.com/@aiDotEngineer — the conference channel. World's Fair 2025 talks are the single best free resource on production agents. Watch the Anthropic, OpenAI, and Sierra talks first.
- **Anthropic** — official YouTube — Claude Code walkthroughs, MCP tutorials, agent patterns. Short and high-quality.
- **Skip the influencer tier:** Matt Wolfe and AI Jason are entertaining but mostly tool-of-the-week content. Useful for keeping current on the consumer tool surface; don't mistake it for depth.

---

## 6. Communities

- **Latent Space Discord** — the AI engineer hangout. Job board, paper discussions, builder community.
- **AI Engineer Foundation / World's Fair Slack** — alumni network from the conference; get an invite if you watch the talks.
- **MLOps Community Slack** — broader ML/ops community; AI subchannels are active and operationally focused.
- **Maven cohort Discords** — for any Maven course you take, the alumni Discord usually outlasts the cohort. The Hamel/Shreya alumni group is especially strong.
- **UK-specific:** the FCA AI Lab community and Tech Nation's AI cohorts. Worth tracking even from outside.

---

## 7. Frameworks & Mental Models to Have on the Tip of Your Tongue

Capital on Tap will ask you "how would you assess where we are with AI?" Have these ready:

- **Gartner 5-level AI Maturity Model:** Awareness → Active → Operational → Systemic → Transformational. Most enterprises are at Active/Operational. The leap from pilots to production is the painful one — and it's where an Adoption Lead earns their salary.
- **MIT CISR AI Maturity stages** — only 7% of enterprises reach the final "AI is in every decision" stage. Stat worth knowing.
- **MITRE Six Pillars** (Ethics; Strategy & Resources; Organization; Technology Enablers; Data; Performance & Application) — useful checklist for "what do we need to put in place?"
- **The four agentic design patterns** (Reflection, Tool Use, Planning, Multi-Agent Collaboration) — Andrew Ng's framing, now standard.
- **The expanded six patterns:** add Orchestrator-Worker and Evaluator-Optimizer. These two are what most production agent systems actually look like.
- **Context engineering** — the emerging term (2025–2026) for how you shape what an agent "knows" at each step. ACE (Agentic Context Engineering) framework is worth name-dropping.
- **Human-in-the-loop oversight as ROI driver** — McKinsey/Stanford finding: 65% of high-performing AI orgs have defined HITL processes vs. 23% of laggards.

---

## 8. Practitioners to Follow

The 12 highest-signal voices for this role profile:

1. **Ethan Mollick** (Wharton) — research-driven adoption insight. Twitter + Substack.
2. **Simon Willison** — engineering-grounded practitioner. Blog daily.
3. **Hamel Husain** — evals expert; ex-Airbnb/GitHub ML.
4. **Shreya Shankar** — AI eval research; UC Berkeley.
5. **Andrew Ng** — DeepLearning.AI, agentic patterns.
6. **swyx (Shawn Wang)** — Latent Space; tracks the AI engineer field.
7. **Chip Huyen** — author of AI Engineering; ex-NVIDIA, Snorkel.
8. **Allie K. Miller** — strongest LinkedIn voice on the people/process side of adoption. Vendor frameworks, ROI calculators.
9. **Cassie Kozyrkov** — ex-Google Chief Decision Scientist; rigorous on decision-quality framing.
10. **Marily Nika** — AI PM at Google; practical AI PM playbooks.
11. **Aman Khan / Arize team** — production AI observability, evals.
12. **Dan Shipper** — operator's view of running an AI-native company.

Bias your follows toward people who are *currently shipping*. Skip the "AI explained" influencers who haven't built anything since 2023.

---

## 9. UK / Regulated Industries — Capital on Tap-specific

- **FCA AI Lab and "AI and the FCA: our approach"** — https://www.fca.org.uk/firms/innovation/ai-approach — read this twice before the interview. The FCA is *not* introducing bespoke AI rules; they're applying existing frameworks (Consumer Duty, SM&CR). Knowing this is table stakes.
- **Bank of England / FCA AI in Financial Services Survey (Nov 2024, updated 2025)** — 75% of UK financial firms are already using AI, +10% planning within 3 years. 59% report measurable productivity gains. These are the stats Capital on Tap leadership will be quoting.
- **Senior Managers & Certification Regime (SM&CR) and AI accountability** — the FCA is publishing 2026 guidance on senior-manager accountability for AI-caused harm. As an Adoption Lead, you don't own this, but you'll be the person operationalizing it. Be ready to discuss governance, audit trails, and HITL design.
- **UK AI Safety Institute / AI Security Institute** — research outputs. Worth knowing exists; not required reading.
- **Industry watering holes:** Tech Nation Fintech, Innovate Finance, the FCA's CEO speeches on fintech innovation. Sign up for FCA newsletters; quote one in your interview.

---

## If you only had 20 hours

**Hours 1–3:** Read *Co-Intelligence* (Mollick). Frames everything else.
**Hours 4–7:** Watch Andrew Ng's Agentic AI course (audit free), focus on the four patterns. Take notes you can paraphrase aloud.
**Hours 8–10:** Anthropic Academy — MCP + Agent Skills courses. Build one MCP server end-to-end (you already have Cowork, so just extend it). This is the build artifact you bring to interviews.
**Hours 11–13:** Read FCA's "AI and the FCA: our approach" + skim the BoE/FCA 2024 survey. Capital-on-Tap-specific. Memorize 3 stats.
**Hours 14–16:** Listen to Latent Space episodes featuring Hamel Husain on evals and Simon Willison on agentic engineering. Read Hamel's evals FAQ at hamel.dev.
**Hours 17–19:** Skim the Stanford Enterprise AI Playbook (51 case studies). Pick 2 case studies that map onto fintech and be able to retell them in 90 seconds each.
**Hour 20:** Write a 1-pager: "If I were the AI Adoption Lead at Capital on Tap, here's what I'd do in my first 90 days." This is your interview centerpiece.

## If you have 3–6 months

**Month 1 — Foundations.** *Co-Intelligence* + Anthropic Academy (all four) + Andrew Ng Agentic AI. Subscribe to One Useful Thing, Latent Space, Simon Willison, and Lenny's. Start a daily 30-min reading habit.

**Month 2 — Engineering depth.** Read *AI Engineering* (Huyen) cover-to-cover. Build a real agent — not a toy — using MCP and Claude Code. Ship it (open-source it on GitHub if possible). Start writing about what you learn.

**Month 3 — Evals and production rigor.** Take the Hamel/Shreya Maven course (or read the book + watch the Lenny's Podcast episodes if budget is tight). Apply evals to the agent you built in Month 2. Write up the methodology publicly.

**Month 4 — Adoption and change management.** Read the Stanford Enterprise AI Playbook + skim *All-In on AI*. Pick 3 case studies and write detailed teardowns. Follow Allie K. Miller and Cassie Kozyrkov closely on LinkedIn. Begin networking — Latent Space Discord, MLOps Community.

**Month 5 — UK/fintech specialization.** FCA documents, BoE/FCA survey, two or three FCA AI Lab speeches. Join Innovate Finance events. Reach out to 5 people who currently hold "AI Lead" / "Head of AI" roles at UK fintechs and ask them what surprised them in the first 6 months.

**Month 6 — Output.** Write 3 LinkedIn posts or a Substack with original synthesis: an AI maturity assessment for UK fintechs; a teardown of one Capital on Tap-style use case (collections, underwriting, customer service); a piece on how SM&CR meets agentic AI. This is what makes you visible to recruiters and credible to interviewers.

---

## Honest meta-note

Most of the value is in **building, shipping, writing, and getting reps with real evals** — not in collecting certificates. If forced to choose between the Reforge $2,000 and 100 hours of building a real Claude/MCP system in your own domain plus writing about it, take the build. The interview signal of "I shipped this" beats every cohort badge except possibly Hamel & Shreya's evals course (which is genuinely exceptional).

You already have most of the practitioner toolkit. The gap is vocabulary (the four patterns, evals, maturity models), evidence of structured shipping (one or two real artifacts you can demo), and UK-regulator literacy. Twenty focused hours closes most of that gap.
