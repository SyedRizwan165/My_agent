# AI Executive Assistant 🤖

A sophisticated personal AI assistant built using the [PHI](https://github.com/phidatahq/phidata) framework, combining multiple specialized agents for comprehensive personal and business support.

![AI Assistant Demo](C:\Users\WINDOWS10\Desktop\my_agent\Agent_Business_plan.png)
![AI Assistant Demo](C:\Users\WINDOWS10\Desktop\my_agent\Ai_Assistant.png)
## Features 🌟

- **Multi-Agent Architecture**:
  - 🧠 Financial Analyst: Stock analysis, market trends, company valuations
  - 🔍 Research Specialist: Web search, data gathering, source verification
  - 🧮 Operations Manager: Advanced calculations, resource optimization
  - 📰 Media Analyst: News monitoring, video content analysis

- **Core Capabilities**:
  - Real-time financial data processing
  - Web research with source validation
  - Complex mathematical calculations
  - News article and video content summarization
  - Markdown-formatted responses with tables and sources

## Tech Stack ⚙️

- **Framework**: [PHI](https://github.com/phidatahq/phidata)
- **LLM**: OpenAI GPT-4o
- **Tools**:
  - DuckDuckGo Search
  - Yahoo Finance (yfinance)
  - Newspaper4k
  - YouTube Transcript API
  - Advanced Calculator

## Installation 💻

1. **Clone repository**:
   ```bash
   git clone https://github.com/yourusername/ai-executive-assistant.git
   cd ai-executive-assistant

2. **Install dependencies**:
```bash
pip install phi python-dotenv duckduckgo-search yfinance newspaper4k youtube-transcript-api
```


3. **Configuration**:
Create .env file with your OpenAI API key:
```bash
OPENAI_API_KEY=sk-your-api-key-here
```
 
4. **Usage 🚀**
Run the assistant:
```bash
python assistant.py
```