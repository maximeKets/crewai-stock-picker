---
title: CrewAI Stock Picker
emoji: 📈
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
pinned: true
hf_oauth: true
---
<div align="center">
  <h1>📈 CrewAI Stock Picker</h1>
  <p><em>An autonomous multi-agent system that researches trending stocks and picks the best investment.</em></p>

  [![GHCR](https://img.shields.io/badge/GHCR-Ready-2ea44f?logo=github)](https://github.com/maximeKets/crewai-stock-picker/packages)
  [![DockerHub](https://img.shields.io/badge/DockerHub-Ready-2496ed?logo=docker)](https://hub.docker.com/r/maximeks/crewai-stock-picker)
  [![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
  [![CrewAI](https://img.shields.io/badge/CrewAI-1.12.2-orange.svg)](https://crewai.com)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
  [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/maximeKets/crewai-stock-picker/graphs/commit-activity)
</div>

---

## 📖 Overview

**CrewAI Stock Picker** is a cutting-edge, autonomous AI project built on the [crewAI](https://crewai.com) framework. It leverages a hierarchical team of specialized AI agents to scan the internet for trending companies, conduct deep financial research, and ultimately select the best equity investment.

The final decision is instantly delivered to you via a custom **Push Notification Tool**, followed by a comprehensive markdown report detailing the investment rationale.

## ✨ Features

- 🕵️‍♂️ **Market Scouting**: Automatically finds companies trending in the news in any given sector.
- 📊 **Deep Financial Research**: Generates comprehensive analysis reports (market position, future outlook, investment potential) for trending stocks.
- 🎯 **Intelligent Equity Selection**: Compares candidates and selects the single most promising investment opportunity.
- 📱 **Instant Alerts**: Uses a custom tool (`PushNotificationTool`) to send push notifications with the final stock pick and a 1-sentence rationale.
- 📝 **Structured Outputs**: Produces organized JSON datasets and clear Markdown decision reports utilizing `pydantic` models.

## 🤖 The Crew (Agents)

The system operates using a **Hierarchical Process** overseen by an AI Manager:

1. **Manager**: Coordinates the workflow, delegating research and decision-making tasks to the team.
2. **Trending Company Finder** (`trending_company_finder`): Scours the web (using SerperDevTool) for 2-3 hot companies currently in the news.
3. **Financial Researcher** (`financial_researcher`): Dives deep into the fundamentals and prospects of the identified companies.
4. **Stock Picker** (`stock_picker`): Synthesizes the research, makes the final investment call, and alerts the user.

## 🚀 Getting Started

### Prerequisites

- Python `>=3.10, <3.14`
- [uv](https://docs.astral.sh/uv/) (Extremely fast Python package installer and resolver)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maximeKets/crewai-stock-picker.git
   cd crewai-stock-picker
   ```

2. **Install dependencies:**
   This project uses `uv` for dependency management. If you don't have it, install it via `pip install uv`.
   ```bash
   crewai install
   ```

3. **Environment Setup:**
   Copy the example environment file and add your API keys.
   ```bash
   cp .env.example .env
   ```
   *Make sure to configure your `OPENAI_API_KEY` and any keys required for Serper and push notifications in the `.env` file.*

## ⚡ Usage

To kickstart the AI crew and begin the autonomous stock-picking process, run:

```bash
crewai run
```
*(Alternatively, use `uv run crewai_stock_picker`)*

### Outputs
Once the run is complete, check the `output/` directory for the results:
- `output/trending_companies.json`: The list of companies found.
- `output/research_report.json`: Deep-dive research data.
- `output/decision.md`: The final investment recommendation and rationale.

## 🛠️ Project Structure

```text
crewai-stock-picker/
├── pyproject.toml
├── src/crewai_stock_picker/
│   ├── config/
│   │   ├── agents.yaml      # Agent definitions and backstories
│   │   └── tasks.yaml       # Task definitions and expected outputs
│   ├── tools/
│   │   └── push_tool.py     # Custom Push Notification Tool
│   ├── crew.py              # CrewAI setup (Agents, Tasks, and Crew initialization)
│   └── main.py              # CLI entry point
└── output/                  # Generated research and reports
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/maximeKets/crewai-stock-picker/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🐳 Déploiement via Docker

Ce projet est distribué sous forme d'image Docker multi-architecture (AMD64 / ARM64).

```bash
# 1. Récupérer la dernière image depuis GitHub Container Registry
docker pull ghcr.io/maximeKets/crewai-stock-picker:latest

# 2. Lancer le conteneur sur le port Gradio (7860) avec vos API Keys
docker run -p 7860:7860 \
  -e OPENAI_API_KEY=your_key \
  -e SERPER_API_KEY=your_key \
  ghcr.io/maximeKets/crewai-stock-picker:latest
```

---
<div align="center">
  <i>Built with ❤️ using <a href="https://crewai.com">crewAI</a></i>
</div>
