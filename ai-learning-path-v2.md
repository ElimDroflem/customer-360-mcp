# AI Learning Path v2 — Indie, Hands-On, Portfolio-First

**For:** Corey, mid-career UK operator targeting AI Adoption Lead / AI Operations Manager / Founding AI Automation roles
**Constraint:** ~£30/month subscription budget, occasional one-off purchases £50–200, NO £1k+ courses
**Goal:** ship interview-ready portfolio pieces in the next 8 weeks (Capital on Tap interview imminent)
**Filter:** indie creators > big platforms; build artifacts > certificates; current 2025–2026 only

---

## 1. GitHub-based learning paths (free, build-to-portfolio)

These are the strongest signal-to-noise resources for an architect-track operator. Free, current, and what you build is the portfolio.

### Anthropic Cookbooks — `anthropics/claude-cookbooks`
The single most relevant resource for an MCP builder. Notebooks covering tool use, sub-agents, evals, RAG, multimodal, computer use. Aligned with Capital on Tap's likely tech stack since they use Claude. **Build:** pick 2–3 notebooks and re-implement with your own dataset. **Time:** 2–4 hours each. **Portfolio:** "I shipped X using pattern Y from the Anthropic cookbook." High signal.
https://github.com/anthropics/claude-cookbooks

### OpenAI Cookbook — `openai/openai-cookbook`
Same idea on the other side of the fence. Less relevant for the Anthropic-aligned interview but worth one or two notebooks for "I'm framework-agnostic" credibility. https://cookbook.openai.com

### Hugging Face Agents Course — `huggingface/agents-course`
Free, modular, currently delivering. Builds across smolagents, LlamaIndex, LangGraph and ends with a GAIA-benchmark agent you publish to a Hugging Face Space. **Time:** ~30–40 hours over 4 units. **Portfolio:** a deployed agent on HF Spaces with a public leaderboard score. The most credible free agentic course in 2026. **Highly recommended.**
https://huggingface.co/learn/agents-course/

### Hugging Face MCP Course — `huggingface/mcp-course`
Built with Anthropic. Free. Walks through MCP from scratch and ends with you publishing servers. Direct overlap with Corey's current Customer 360 build — finishing this would let him cite the course in interview while talking through his MCP. **Time:** 8–12 hours. https://huggingface.co/learn/mcp-course/

### Sebastian Raschka — `rasbt/LLMs-from-scratch` and `rasbt/reasoning-from-scratch`
The book + repo combo that's become the canonical "I actually understand transformers" credential. **Honest assessment for Corey:** this is more depth than an AI Operations Lead needs. Skip the full course; skim chapters 1–4 to be conversant about tokenization, attention, fine-tuning. 3–5 hours, not 50.
https://github.com/rasbt/LLMs-from-scratch

### Andrej Karpathy — `karpathy/nn-zero-to-hero`
Same caveat. Beautiful pedagogy, transformative if you want to be an ML engineer, **overkill for an AI Adoption role**. Watch the first "makemore" lecture (free YouTube) for the experience and move on.
https://github.com/karpathy/nn-zero-to-hero

### CrewAI examples — `crewAIInc/crewAI-examples`
Working multi-agent flows you can fork and adapt: meeting assistant, lead scoring, content creator, email auto-responder. **Portfolio play:** fork the lead-scoring flow, point it at synthetic Capital on Tap merchant data, ship it. https://github.com/crewAIInc/crewAI-examples

### E2B Cookbook — `e2b-dev/e2b-cookbook`
For agent code execution / sandboxing. Useful if your portfolio piece involves an agent that runs code. Less critical for Corey's near-term goals.
https://github.com/e2b-dev/e2b-cookbook

### Aishwarya Naresh Reganti — `aishwaryanr/awesome-generative-ai-guide`
Curated 60+ projects with tutorials, plus interview prep notebooks. The "60 GenAI Projects to Boost Your Resume" list is genuinely a project menu. Good for picking your portfolio targets. https://github.com/aishwaryanr/awesome-generative-ai-guide

---

## 2. Indie creator courses ($50–300 or sub <$50/mo)

The brutal truth: most of the best-known indie creators in this space (Hamel, Jason Liu, Greg Kamradt) have moved into the £1k+ Maven cohort tier you're trying to avoid. Their **free** content is still excellent and what you should consume.

### Jason Liu — Instructor library + free posts
Library: https://github.com/jxnl/instructor (free, MIT)
His **free** writing on RAG evals at https://jxnl.co is some of the best operator-grade thinking on building reliable AI features. The Maven RAG course is $1,500+; **skip it**, read the blog and use Instructor in a project. Signal: very high. The library is itself the portfolio: "I use Instructor for structured outputs in my MCP."

### Hamel Husain — `hamel.dev` blog + free Substack
The Maven Evals course (with Shreya Shankar) is $2k and expanding. The **free** "LLM Evals FAQ" post is ~150 pages of equivalent material and is genuinely the operator's reference doc on evals. https://hamel.dev/blog/posts/evals-faq/ — read it twice, build a small eval harness for your MCP off the back of it. That's a portfolio piece by itself.

### Eugene Yan — `eugeneyan.com` (free)
"Patterns for Building LLM-based Systems & Products" is the canonical operator's handbook: evals, RAG, fine-tuning, caching, guardrails, defensive UX, feedback loops. Free. Co-author of the "What we've learned from a year of building with LLMs" series at applied-llms.org. https://eugeneyan.com/writing/llm-patterns/ — **highest signal piece of free writing in this space.** Re-read for interview prep.

### Cameron Wolfe — Deep (Learning) Focus Substack
Free tier publishes the bulk of content; paid tier (~$10/mo) gets you a few deep-dive bonus posts. Not strictly "build along," more "research explainer." Useful for talking-the-talk depth without doing maths. https://cameronrwolfe.substack.com/

### Sahar Mor — AI Tidbits
Paid tier ~$10/mo. Posts a "Coding with AI" guide (April 2025) that's genuinely practitioner-level. AI Builders Series is the relevant section. **Worth the £8/mo for 3 months while you're in build mode.** https://www.aitidbits.ai/

### Sander Schulhoff — Learn Prompting (free) + AI Red-Teaming Masterclass (Maven)
The Learn Prompting docs are free and extensive. The Red Teaming Masterclass on Maven runs at the £1k+ tier — **skip**. Read the free docs, particularly advanced prompting techniques, and reference them in your MCP guardrails design. https://learnprompting.org/

### swyx + Noah Hein — "Level Up From Software Engineer to AI Engineer" on Maven
3-week course, ~$1k, **skip** — but the **free** "Latent Space University" 7-day email course at https://www.swyx.io is a useful primer. The 2025 AI Engineer Reading List by swyx is a curated path: https://www.latent.space.

### Cassie Kozyrkov — "Decision-Making with ChatGPT" on Maven + free Substack
Decision Intelligence Substack is free and an excellent angle for an AI Adoption Lead role — she frames AI from the leadership/decision-making side, which is exactly your archetype. https://decision.substack.com/. The Maven course is in the $300–500 range, debatable; the LinkedIn Learning "Decision Intelligence" course is much cheaper if you have access via Capital on Tap once hired.

### Aakash Gupta — "Aakash's Bundle" $150/year
$150/year for an AI PM bundle. The bundle includes prompt libraries, frameworks, and an "AI PM certificate" with a 5-hour video course. **Honest take:** the AI PM material here is operator-flavored, not engineer-flavored — closer to your target archetype than most engineering courses. Worth the £120 if you treat it as a focused 2-week deep dive. https://www.news.aakashg.com/

---

## 3. YouTube build-along series (free, signal > noise)

### Sam Witteveen — `@samwitteveenai`
Google Developer Expert, builds end-to-end agentic systems. Series on autonomous agents from 2023 onward. Genuine engineer, not a tool-of-the-week fluffer. **High signal.** https://www.youtube.com/@samwitteveenai

### James Briggs — `@jamescalam`
"LangChain Mastery 2025" 5-hour free course on YouTube. RAGAS evaluation tutorials. Aurelio AI founder. **High signal**, especially his evals content. https://www.youtube.com/c/jamesbriggs

### AI Makerspace — `@AI-Makerspace`
Free weekly live build sessions. Greg Loughnane and Chris Alexiuk. They run a paid bootcamp ($$$) but the YouTube lives are free and they post all code on GitHub at https://github.com/AI-Maker-Space. The cadence — a real production-grade build every week — is rare. **Highly recommended for ongoing learning while building.** https://www.youtube.com/@AI-Makerspace

### Greg Kamradt — `@dataindependent`
Original "Needle in a Haystack" creator, ARC Prize co-lead. His older LangChain tutorials are slightly dated; his newer talks at AI Engineer World's Fair are excellent. **Selective watch — pick conference talks, skip random shorts.**

### Patrick Loeber — `patloeber.com` and YouTube
Now creating content with Google Developers (since Sept 2025). Solid pedagogy for AI/ML basics. Useful if you want to refresh fundamentals quickly. **Not the most "operator-y" but high quality.**

### Matt Williams — `@technovangelist`
Founding maintainer of Ollama. Tutorials on running local AI, MLX on Apple Silicon, fine-tuning. Useful if your portfolio includes anything local-first / privacy-preserving (a big angle for UK fintech given GDPR). **High signal.**

### AI Jason — `@AIJasonZ`
Mostly experiment-of-the-week content. Some good stuff but **often too shallow for an architect track.** Watch selectively, don't subscribe to the firehose.

### David Shapiro
Big channel, but became increasingly AGI-speculation focused. **Skip for portfolio purposes.**

### AI Engineer (conference talks) — `@aiDotEngineer`
World's Fair and Summit talks are gold for hearing how real teams ship. Not a structured series but **mandatory background watching.**

---

## 4. Build-along communities

### BuildClub.ai
Free Slack community + free challenges + paid certifications. Active in 2026. Good for accountability and sharing builds. Challenge-based learning is closest to "ship a portfolio piece every 2 weeks." https://buildclub.ai/

### AI Engineer Discord (via Latent Space)
Free. Active. Where AI engineers actually hang out. Lurk for the conversations, post your MCP for feedback. https://www.latent.space/

### Hugging Face Discord
Free. The Agents Course has its own active Discord with weekly live sessions during course delivery. Best community for "I'm working through course X, who else?"

### AI Makerspace Discord
Free entry tier. Some content gated to paid bootcamp. Active.

### r/LocalLLaMA + r/LangChain on Reddit
Free. r/LocalLLaMA particularly is operator-heavy (people running real systems) rather than influencer-heavy.

---

## 5. Project-based platforms ($15–50/month)

### Boot.dev — ~$24/mo
**Strongest project-based platform for AI work right now.** "Build an AI Agent in Python" course where you ship a Cursor-Agent-Mode-style code editor. Plus a recent RAG course covering keyword + semantic search end-to-end. All actual code, no lectures. **Strong recommendation if you want one paid sub.** https://www.boot.dev/courses/build-ai-agent-python

### Frontend Masters — $39/mo
"AI Engineering" by Scott Moss (Netflix). You build an Excalidraw-with-AI agent app, with eval harness, context engineering, RAG. Very portfolio-shaped. Caveat: requires comfort with TypeScript/React. https://frontendmasters.com/courses/ai-engineering/

### Educative.io — ~$15/mo
Text-based interactive labs (no video). Their "Grokking Generative AI System Design" is closest to what you want. Cheaper than Frontend Masters; less polished. Reasonable if Boot.dev / Frontend Masters don't work for you.

### Replit (free starter, paid tiers)
Free starter plan has the AI Agent. Replit Learn is a free path. **Most useful as a deployment target for portfolio pieces, not as a course platform.**

### Pluralsight, DataCamp, Udemy
**Skip for portfolio purposes.** Too many fluff courses, too "certificate factory."

---

## 6. Substacks / paid blogs that publish actual artifacts

The pattern across this space: paid tiers usually buy you ~10–20% more content. Most build artifacts (repos, design docs) are public.

| Newsletter | Cost | Best for | Signal |
|---|---|---|---|
| Eugene Yan (eugeneyan.com) | Free | Operator patterns, evals | Highest |
| Hamel Husain (hamel.dev) | Free | Evals, ML ops | Highest |
| Cameron Wolfe (Deep Learning Focus) | Free / $10mo | Research explainers | High |
| Sahar Mor (AI Tidbits) | Free / ~$10mo | Builder series, news | High |
| Sebastian Raschka (Ahead of AI) | Free / $10mo | Model architecture | High (depth) |
| Latent Space (swyx) | Free | Field state-of-the-art | High |
| Aakash Gupta (Product Growth) | Free / $150yr | AI PM operator angle | Medium-High |
| Cassie Kozyrkov (Decision Intelligence) | Free | Leadership/adoption framing | High for your archetype |

**Recommendation:** all the free ones, plus AI Tidbits paid for 2–3 months while you're in active build mode.

---

## 7. Hackathons and build challenges (free, public artifact)

This is the best portfolio-yield-per-hour activity available to you. Pick one in the next 8 weeks.

### Lablab.ai — `lablab.ai`
Runs ~monthly themed AI hackathons. Free. Demo-day gives you a public Devpost/Lablab page. Upcoming relevant ones:
- **Transforming Enterprise Through AI** (May 11–19, 2026) — directly fintech/enterprise relevant. **Strong fit.**
- **AI Agent Olympics** (May 13–20, 2026) — agentic systems, $$ prize pool.
- **Web Data Access Hackathon** (May 25–31, 2026)

https://lablab.ai/ai-hackathons

### Anthropic Hackathons
Anthropic ran "Built with Opus 4.6" in Feb 2026 ($100k credit prize). They run roughly quarterly. Watch https://www.anthropic.com and https://devpost.com for the next London or remote one. **Highest credibility hackathon in the Claude ecosystem** — winning or even submitting one is a hiring signal in itself.

### DevPost AI category
https://devpost.com/c/artificial-intelligence — filter by "ongoing" / "upcoming." Several fintech-flavored ones running May–June 2026 (DevNetwork, ALGOfest, BluePrint).

### BuildClub challenges (recurring, free)
https://campus.buildclub.ai/challenges — smaller scope, lower stakes, faster feedback.

---

## 8. MCP / agent architecture / context engineering (your current build)

### Anthropic Skilljar — "Introduction to Model Context Protocol" (free)
Free, official, current. The course Corey should finish first if he hasn't. https://anthropic.skilljar.com/introduction-to-model-context-protocol

### DeepLearning.AI × Anthropic — "MCP: Build Rich-Context AI Apps" (free)
Free 1h38m course taught by Elie Schoppik (Anthropic). You build a paper-search MCP server with FastMCP, deploy remotely, integrate with Claude Desktop. **Direct alignment with the current Customer 360 MCP build.** https://learn.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic/

### Smithery — `smithery.ai`
MCP registry + CLI. Use it to publish your Customer 360 MCP once it's working. Publishing to Smithery is itself a portfolio artifact. Build docs at https://smithery.ai/docs/build/getting-started

### Vellum AI Blog
Excellent operator-grade writing on agent architectures, context engineering, multi-agent systems. Free, no signup. https://www.vellum.ai/blog — particularly the "Agentic Workflows in 2026" guide and "Multi Agent Systems With Context Engineering."

### `davidkimai/Context-Engineering` GitHub
First-principles handbook on context engineering inspired by Karpathy. Active 2025/26 repo. Free. Good for breadth on the discipline.

### Letta (formerly MemGPT) tutorials
Memory-focused agent framework. Tutorials at https://docs.letta.com/. Useful if your portfolio piece needs longer-term memory than naive RAG.

### Modal Labs documentation
Best operator's guide to deploying serverless AI workloads. Free, used in production by many teams. https://modal.com/docs

---

## 9. AI Adoption / AI Operations specifically (the operator angle)

This is where the original report under-served you. Engineering content dominates Google results; operator content is harder to surface.

### Allie K. Miller — `alliekmiller.com`
The clearest operator voice in this space. Frameworks: CRAFT, Microtasker→Copilot→Delegate→Teammate, Dot-Dash-Star. Maven course "AI for Business Leaders" is in the $500–1500 range. **Her free LinkedIn and YouTube content is enough** for talking points. **Memorize the four-modes framework before the Capital on Tap interview** — it's the cleanest mental model for explaining AI rollout to non-technical execs. https://www.alliekmiller.com/

### Cassie Kozyrkov — Decision Intelligence
Free Substack at https://decision.substack.com/. "Four Pillars of Trust" framework (competence, integrity, benevolence, charisma) — useful interview vocabulary. Maven course "Decision-Making with ChatGPT" is mid-tier price; debatable.

### Aakash Gupta — Product Growth
"Complete AI Product Manager Transition Guide (2025)" at https://www.aakashg.com/the-complete-ai-product-manager-transition-guide-2025-edition/. Free. Operator-flavored. The bundle ($150/yr) is debatable but you'd get prompt libraries you could reference.

### UK / fintech / regulated specifically
- **King's College London — AI Governance Leadership Programme**: pricey but credible. Mention it as "on my watchlist" in interview.
- **Imperial Executive Education — AI in Finance**: same.
- **UK Finance — AI Governance training**: industry body course, fintech-specific.
- **AIGP certification (IAPP)**: recognised AI governance credential, ~$500. Worth it if you go further into governance roles after Capital on Tap.
- **Beaumont Capital Markets — UK AI in Financial Services 2025 trends report**: free read, gives you UK-specific regulatory talking points (FCA, EU AI Act intersection). Read before interview.

### Lenny's Newsletter — free + paid ($15/mo)
Lenny Rachitsky's interviews with Hamel Husain, Sander Schulhoff and others are some of the cleanest "AI for product/operator" content available. Free podcast tier is enough.

---

## 10. Build-in-public practitioners worth following

For the "follow them and absorb" learning path. All free, signal-rich:

1. **swyx** (@swyx) — Latent Space, AI Engineer field-of-view
2. **Hamel Husain** (@HamelHusain) — evals, ML ops practitioner
3. **Eugene Yan** (@eugeneyan) — patterns, applied ML
4. **Jason Liu** (@jxnlco) — Instructor, RAG, structured outputs
5. **Logan Kilpatrick** (@OfficialLoganK) — Google AI Studio product lead, ships in public
6. **Greg Kamradt** (@GregKamradt) — ARC Prize, evals, Needle-in-Haystack
7. **Aishwarya Naresh Reganti** — agentic AI applied teaching
8. **Allie K. Miller** (@alliekmiller) — AI adoption operator
9. **Sebastian Raschka** (@rasbt) — model architecture depth
10. **Chip Huyen** (@chipro) — AI engineering book author, system design depth
11. **Andrej Karpathy** (@karpathy) — taste-maker, occasional drops are gold
12. **Linus Lee** (@thesephist) — independent AI tools/notation builder, taste

Make a Twitter/X list, check daily for 10 minutes. That's the cheapest education in the space.

---

## The 8-week plan: £30/month, 3 portfolio pieces

**Budget reality check:** £30/mo gets you ONE paid sub. The rest is free.

**My pick:** **Boot.dev (~£18/mo)**. Then add **AI Tidbits (~£8/mo)** for current commentary. Total ~£26/mo. The other big sub options (Frontend Masters, Educative) are reasonable substitutes — Boot.dev wins for being most explicitly project-based.

### Weeks 1–2: Get the Customer 360 MCP shippable + finish the cheap free MCP courses
- **Anthropic Skilljar MCP course** (free, ~4 hours) — finish this if not done
- **DeepLearning.AI × Anthropic MCP course** (free, ~2 hours) — directly applicable
- **Read Eugene Yan "Patterns for Building LLM-based Systems & Products"** (free, 2 hours)
- **Read Hamel Husain "LLM Evals FAQ"** (free, 2–3 hours)
- **Build:** finish Customer 360 MCP, write a 1-page README that explicitly maps your design choices to the patterns above ("I added defensive UX as per Eugene Yan / I designed evals as per Hamel"). Publish to Smithery registry.

**Portfolio piece #1: Customer 360 MCP, published, with design doc citing operator patterns.** This is interview-ready.

### Weeks 3–5: HF Agents Course + a fintech-flavored agent
- **HF Agents Course units 1–4** (free, ~25–30 hours) — ship the GAIA-benchmark agent
- **Read Vellum's agentic workflows guide** (free, 1 hour) for vocabulary
- **Build:** while doing HF course, fork CrewAI's lead-scoring example, swap in synthetic Capital-on-Tap-shaped data (small business merchants applying for cards), add a guardrail layer, ship to HF Spaces

**Portfolio piece #2: A fintech-credit-decisioning agent on HF Spaces with leaderboard score from GAIA + a separate fintech demo.** Tells a story specifically aimed at Capital on Tap.

### Weeks 6–8: Hackathon entry + adoption framework artifact
- **Enter Lablab.ai "Transforming Enterprise Through AI" or "AI Agent Olympics"** (free) — the deadline pressure is the point
- **Read Allie K. Miller's free content; memorize CRAFT and four-modes** (free, 1 hour)
- **Build:** the hackathon entry. Choose something operator-flavored — e.g., "AI rollout dashboard for non-technical managers" or "Guardrailed customer-support agent with eval harness for regulated industries."
- **Side artifact:** write a 1500-word "AI Adoption Playbook for UK Fintech" Medium/LinkedIn post citing Allie K. Miller's frameworks, the Beaumont UK fintech regulatory report, and your own MCP build. This is the "AI Adoption Lead" calling card.

**Portfolio piece #3: Hackathon submission + published thought-piece showing operator-level thinking.**

### Reading throughout (in slack time)
- **Cassie Kozyrkov Decision Intelligence Substack** (free) — for adoption-framing vocabulary
- **AI Tidbits paid posts** (£8/mo) — for current state of the field
- **Latent Space podcast** (free) — pick 2 episodes per week, listen on commutes
- **Twitter/X list of the 12 above** — 10 minutes daily

### What NOT to do
- Don't enroll in any of: Maven Hamel Evals course, Maven Jason Liu RAG, Maven swyx AI Engineer, AI Makerspace bootcamp, King's College AI Governance — all £1k+. Useful as benchmarks; not now.
- Don't watch 30-day-AI-mastery YouTube series. They're noise.
- Don't read Sebastian Raschka's full LLMs-from-Scratch book or Karpathy's full nn-zero-to-hero. Skim chapter 1 of each, move on.
- Don't do Coursera/Udemy generic AI courses. Certificate factories.
- Don't try to learn TypeScript+React for Frontend Masters AI Engineering unless you already know them.

### Honest uncertainty I'm flagging
- **AI Tidbits paid value**: I haven't verified the depth of paid posts vs free directly. £8/mo is low risk; cancel after a month if the paid posts don't move you.
- **Boot.dev AI agent course quality 2026**: it's clearly project-based and current, but I haven't audited the specific lessons. Worst case it's still the cheapest project-based option in the market.
- **Lablab.ai hackathon judging quality varies**: smaller hackathons can be lightly judged. The Anthropic-run ones (when they come around) are higher prestige; watch for one in the next 3 months.

---

## TL;DR resource shortlist

**Free, do these now:**
1. Anthropic MCP courses (Skilljar + DeepLearning.AI)
2. HF Agents Course
3. Eugene Yan "Patterns" + Hamel Husain "Evals FAQ"
4. Vellum blog
5. Allie K. Miller's frameworks (free LinkedIn/YouTube)
6. Lablab.ai hackathon entry

**Paid, ~£26/mo total:**
1. Boot.dev (~£18/mo) — Build an AI Agent in Python
2. AI Tidbits (~£8/mo) — current commentary

**Free GitHub repos to fork:**
1. anthropics/claude-cookbooks
2. crewAIInc/crewAI-examples
3. aishwaryanr/awesome-generative-ai-guide
4. e2b-dev/e2b-cookbook

**Twitter/X list:** swyx, Hamel, Eugene Yan, Jason Liu, Allie K. Miller, Aishwarya Naresh Reganti, Logan Kilpatrick, Greg Kamradt, Linus Lee, Karpathy, Chip Huyen, Sebastian Raschka.

Three portfolio artifacts in 8 weeks: Customer 360 MCP shipped + fintech agent on HF Spaces + hackathon entry & operator-angle thought piece. That's an interview-ready package for an AI Adoption / Operations Lead role at Capital on Tap.
