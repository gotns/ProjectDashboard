This is a dashboard for tracking project work progress.

Hardware Selection & Onboarding Configurator
Context: Use this prompt with a conversational AI to choose your host hardware and optimal setup paths before initiating openclaw onboard [01:48].

Prompt:
"I am setting up an OpenClaw autonomous AI agent. Help me determine the best hardware configuration and onboarding parameters based on my resources. I will provide my current constraints. Ask me the following questions one by one to give me a tailored recommendation:

What machine am I planning to run this on (old laptop, dedicated Mac Mini/Studio, or a VPS)?

How many gigabytes of RAM does this machine have?

What is my monthly budget for LLM API tokens?

Do I already have an OpenAI or Anthropic API subscription?
Based on my answers, output the optimal Model Provider (e.g., Anthropic Opus/Sonnet, GPT-5, or Minimax M2.5) and specify if I should route tasks to local open-source models like Qwen Coder or Mistral."

2. Seeding the Agent’s Persona (soul.md & user.md)
Context: OpenClaw relies on plain-text markdown files to govern its identity [06:26]. Paste the output of this prompt directly into your communication channel (Telegram/Discord) once your bot is online to populate its core memory files [08:00].

Prompt:
"Act as an expert AI systems architect. I need to configure the core identity files for my OpenClaw agent. Generate the markdown text for two specific files:

soul.md: Define the persona of an agent named 'Inky' (an autonomous partner, not a passive assistant). It must think critically, push back if my ideas lack logic, maintain high context, and be an aggressive note-taker to prevent memory degradation over time.

user.md: (Leave placeholders for me to fill out) Outline my core professional focus (Content Creation, Software Building, or Portfolio Tracking), my daily workflow preferences, and my standard operating procedures.

Ensure the tone is proactive, highly collaborative, and strictly structured for an LLM to digest upon every session startup."

3. Mission Control Generation
Context: Tina utilizes a custom dashboard as a "Central Monitoring Hub" to track agent tasks, logs, and approvals [08:20]. Instruct your agent via its terminal/chat interface to spin this up.

Prompt:
"Inky, I need you to build a custom 'Mission Control' web dashboard interface to serve as our central hub. The dashboard must include the following distinct tracking modules:

Agent Office: A visual feed showing what active multi-agent processes are executing.

Task Tab: A table tracking active tasks, assigned owners, and a live activity log.

Content Pipeline: A dedicated tab containing a 'Topic Watchlist' (aggregating from Hacker News, X, and Reddit) alongside an 'Approval' workflow.

Memory System: A portal to view long-term memories pulled from memory.md and chronological daily activity logs.

Generate and deploy the code for this UI inside our workspace environment."

4. Discord Multi-Channel Structure Configuration
Context: If transitioning from Telegram to a structured Discord server setup [10:11], use this prompt inside your general Discord server channel once the bot connection is verified.

Prompt:
"Inky, execute an automated server setup script to organize our communication hub. Create the following dedicated text channels with strict permission settings allowing only you and me access:

#general - For direct text communication and manual task execution.

#daily-digest - Where morning briefs and industry news updates are compiled.

#research-deep-dives - For comprehensive analyses on specific topics.

#content-ideas - A queue where you post high-scoring concepts requiring manual approval.

#system-alerts - A protected logging channel for twice-daily automated health and security audits."

5. Multi-Agent System Framework Expansion
Context: To save on token costs and increase performance, the workflow is split into specialized sub-agents [17:01]. Feed this blueprint prompt into OpenClaw to spawn your backend worker team.

Prompt:
"Inky, we need to scale our system from a single agent to a coordinated multi-agent team. Program and initialize five specialized background agents under your command:

Blinky (The Morning Scout): Scans Hacker News, X, and Reddit daily for relevant industry trends. Scores them based on criteria in user.md and logs results.

Pinky (The Research Analyst): Takes high-scoring topics every evening and performs an extensive, data-driven background deep-dive.

Dinky (The Content Producer): Translates approved deep-dives into structured production outlines or operational drafts.

Linky (The Local Builder): Executes software coding tasks. (Rule: Use Claude Opus/Sonnet for architectural planning, but route the bulk execution to a local, free instance of Qwen Coder 8B to save token costs).

Winky (The System Monitor): Runs background tasks, system checks, and handles memory optimization."

6. Security and Memory Preservation Protocols
Context: To avoid memory degradation over time and protect private data, use these instructions to enable automated maintenance routines [20:06].

Prompt:
"Configure a persistent cron job or automated background sequence to execute the following safety and memory optimizations:

Security Audits: Twice daily, parse the official OpenClaw security guidelines (openclaw.ai/security) and cross-reference our configuration. Flag vulnerabilities or available updates directly into the #system-alerts channel.

Memory Consolidation (Dreaming Protocol): Every night, review our interaction histories and daily logs. Summarize temporary context strings, write key takeaways into dreams.md, and elevate critical, permanent rule changes directly into memory.md [21:31]. Ensure you maintain a localized Wiki structure for quick vector searching."

7. Code Stabilization Protocol (Advanced Workflow)
Context: LLM prompt-chaining is inherently unpredictable and prone to drift [23:55]. Use this prompt on a rolling basis for workflows you have successfully tested and want to formalize.

Prompt:
"Inky, look at the multi-agent prompt pipeline we just built for [Insert Workflow Name, e.g., The Daily News Digest]. Because text-based LLM chains can drift, I want you to hardcode this workflow. Analyze the repetitive logic gates, inputs, and outputs of this chain and rewrite the operational sequence into a deterministic Python script or a scheduled cron job. Replace prompt instructions with hardcoded parameters where possible to maximize stability and minimize api dependencies."
