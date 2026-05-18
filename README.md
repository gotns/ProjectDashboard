# Project emCee: Autonomous Multi-Agent Framework

Project emCee is a professional-grade autonomous AI agent system designed to function as a proactive partner rather than a passive assistant. It leverages a specialized multi-agent architecture to handle research, content production, software development, and system maintenance, all monitored through a central "Mission Control" dashboard.

## 🛠 Tech Stack

- **Orchestrator:** PI agent
- **Primary Models:** 
  - `gemma4:31b` (Architectural Planning & High-Level Reasoning)
  - `qwen3.6:27b` (Bulk Execution & Technical Implementation)
- **Database:** SQLite (Memory Portal)
- **Communication:** Discord API
- **Memory Layer:** Markdown-based persistent storage (`soul.md`, `user.md`, `memory.md`, `dreams.md`)

---

## 🧠 System Architecture: Memory Hierarchy

To prevent context drift and memory degradation, emCee utilizes a tiered memory system:

| File | Purpose | Persistence |
| :--- | :--- | :--- |
| `soul.md` | Core Identity, Ethics, and Persona constraints | Permanent |
| `user.md` | User professional focus, SOPs, and preferences | Permanent |
| `memory.md` | Long-term knowledge base and critical rule changes | Permanent |
| `dreams.md` | Nightly consolidated summaries of daily activity | Rotating/Archived |

---

## 🚀 Getting Started (Setup Workflow)

Follow these steps in order to initialize the emCee ecosystem.

### Step 1: Seeding the Persona
Initialize the core identity and user preferences.

**Prompt:**
```markdown
Act as an expert AI systems architect. I need to configure the core identity files for my agent. Generate the markdown text for two specific files:

soul.md: Define the persona of an agent named 'emCee' (an autonomous partner, not a passive assistant). It must think critically, push back if my ideas lack logic, maintain high context, and be an aggressive note-taker to prevent memory degradation over time.

user.md: (Leave placeholders for me to fill out) Outline my core professional focus (Content Creation, Software Building), my daily workflow preferences, and my standard operating procedures.

Ensure the tone is proactive, highly collaborative, and strictly structured for an LLM to digest upon every session startup.
```

### Step 2: Infrastructure Setup (Discord)
Create the communication hub for agent-user interaction.

**Prompt:**
```markdown
Execute an automated server setup script to organize our communication hub. Create the following dedicated text channels with strict permission settings allowing only you and me access:

#general - For direct text communication and manual task execution.
#daily-digest - Where morning briefs and industry news updates are compiled.
#research-deep-dives - For comprehensive analyses on specific topics.
#content-ideas - A queue where you post high-scoring concepts requiring manual approval.
#system-alerts - A protected logging channel for twice-daily automated health and security audits.
```

### Step 3: Mission Control Deployment
Build the visual monitoring hub to track agents and tasks.

**Prompt:**
```markdown
I need you to build a custom 'Mission Control' web dashboard interface to serve as a central hub. The dashboard must include the following distinct tracking modules:

Agent Office: A visual feed showing what active multi-agent processes are executing.
Task Tab: A table tracking active tasks, assigned owners, and a live activity log.
Content Pipeline: A dedicated tab containing a 'Topic Watchlist' (aggregating from Hacker News and Reddit) alongside an 'Approval' workflow.
Memory System: A sqlite portal to view long-term memories pulled from memory.md and chronological daily activity logs.

Generate and deploy the code for this UI inside our workspace environment.
```

### Step 4: Multi-Agent Team Expansion
Scale emCee from a single agent to a coordinated specialized team.

**Prompt:**
```markdown
emCee, we need to scale our system from a single agent to a coordinated multi-agent team. Program and initialize five specialized background agents under your command:

- Blinky (The Morning Scout): Scans Hacker News, X, and Reddit daily for relevant industry trends. Scores them based on criteria in user.md and logs results.
- Pinky (The Research Analyst): Takes high-scoring topics every evening and performs an extensive, data-driven background deep-dive.
- Dinky (The Content Producer): Translates approved deep-dives into structured production outlines or operational drafts.
- Linky (The Local Builder): Executes software coding tasks. 
  (Rule: Use gemma4:31b for architectural planning, but route the bulk execution to qwen3.6:27b to maximize efficiency).
- Winky (The System Monitor): Runs background tasks, system checks, and handles memory optimization.
```

---

## 🛠 Maintenance & Optimization

### Security & Memory Preservation
To ensure the system remains healthy and remembers critical data, execute the following routine.

**Prompt:**
```markdown
Configure a persistent cron job or automated background sequence to execute the following safety and memory optimizations:

1. Security Audits: Twice daily, parse the official security guidelines and cross-reference our configuration. Flag vulnerabilities directly into the #system-alerts channel.
2. Memory Consolidation (Dreaming Protocol): Every night, review our interaction histories and daily logs. Summarize temporary context strings, write key takeaways into dreams.md, and elevate critical, permanent rule changes directly into memory.md. Ensure you maintain a localized Wiki structure for quick vector searching.
```

### Code Stabilization (Anti-Drift Protocol)
When a prompt-based workflow becomes successful, harden it into a deterministic script.

**Prompt:**
```markdown
emCee, look at the multi-agent prompt pipeline we just built for [Insert Workflow Name]. Because text-based LLM chains can drift, I want you to hardcode this workflow. Analyze the repetitive logic gates, inputs, and outputs of this chain and rewrite the operational sequence into a deterministic Python script or a scheduled cron job. Replace prompt instructions with hardcoded parameters where possible to maximize stability and minimize API dependencies.
```
