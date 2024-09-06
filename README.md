# Melt: GenAI Networking Application

**Melt** is an AI-driven networking app designed to autonomously retrieve and analyze LinkedIn profiles using advanced Generative AI techniques like ReAct prompting. The app leverages the power of **OpenAI**, **Tavilly**, **Proxy URL**, and **LangChain** to provide users with actionable insights to enhance networking opportunities on LinkedIn.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

---

## Features

- Autonomous LinkedIn profile retrieval and analysis.
- AI-driven insights using **LLM** and **ReAct prompting**.
- Streamlined backend using **Flask** for API handling.

---

## Tech Stack

- **Backend**: Flask, Python
- **AI Models**: OpenAI, LangChain
- **Frontend**: HTML/CSS (Optional, if any UI is involved)
- **APIs**: Tavilly, Proxy URL

---

## Installation

- Clone the repository:

   ```bash
   git clone https://github.com/your-username/melt-genai-networking.git
   cd melt-genai-networking

- Create and activate a virtual environment:

```bash
pipenv install
pipenv shell
```

## Usage
- Set up the API keys. Reference the .env.example file fore reference.

```bash
LINKEDIN_API_KEY=your_linkedin_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILLY_KEY=your_tavilly_key
```

- Run the App
```bash
python app.py
```

The AI agents will autonomously scrape and analyze the LinkedIn profiles, providing actionable networking insights and icebreakers.

## Configuration
OpenAI API Key: Get your API key from OpenAI.
Tavilly API: For profile data access, you need to generate a Tavilly API key.
Proxy URL: Configure the proxy url api for LinkedIn scraping.
