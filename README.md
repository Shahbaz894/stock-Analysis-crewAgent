# Marketing Post Crew

## Overview
Marketing Post Crew is an AI-powered system built using CrewAI. It leverages multiple AI agents to research market strategies, generate campaign ideas, and create compelling marketing copy. This system is designed to automate and enhance marketing content creation using OpenAI's GPT models.

## Features
- **Automated Market Research:** Uses AI agents to analyze and understand market trends.
- **Marketing Strategy Generation:** Develops effective marketing strategies based on data.
- **Creative Campaign Ideation:** Generates innovative campaign ideas.
- **Copywriting Assistance:** Produces high-quality marketing content.
- **Web Scraping & Search Integration:** Uses external tools to fetch relevant data.

## Technologies Used
- **Python 3.10+**
- **CrewAI** for multi-agent orchestration
- **OpenAI GPT-4/GPT-3.5** for natural language processing
- **SerperDevTool** for Google search integration
- **ScrapeWebsiteTool** for web scraping
- **Pydantic** for data validation
- **YAML** for configuration management
- **Logging** for debugging and tracking

## Installation
### Prerequisites
Ensure you have Python 3.10 or later installed.

### Clone the Repository
```bash
git clone https://github.com/your-repo/marketing-post-crew.git
cd marketing-post-crew
```

### Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the project root and add the following variables:
```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

## Project Structure
```
marketing-post-crew/
│-- config/
│   ├── agents.yaml          # Configuration for AI agents
│   ├── tasks.yaml           # Configuration for tasks
│-- logs/
│-- src/
│   ├── main.py              # Entry point for running the AI agents
│   ├── crew.py              # CrewAI orchestration logic
│   ├── logger.py            # Logging setup
│   ├── utils.py             # Utility functions
│-- .env                     # Environment variables
│-- requirements.txt         # Project dependencies
│-- README.md                # Documentation
```

## Configuration
### Agents Configuration (`config/agents.yaml`)
Define AI agents and their roles.
```yaml
lead_market_analyst:
  name: "Lead Market Analyst"
  description: "Researches market trends and competitors."
  model: "gpt-4"
  temperature: 0.7

chief_marketing_strategist:
  name: "Chief Marketing Strategist"
  description: "Develops marketing strategies."
  model: "gpt-4"
  temperature: 0.7

creative_content_creator:
  name: "Creative Content Creator"
  description: "Writes engaging marketing content."
  model: "gpt-4"
  temperature: 0.7
```

### Tasks Configuration (`config/tasks.yaml`)
Define the tasks assigned to each agent.
```yaml
research_task:
  description: "Conducts market research and analysis."

marketing_strategy_task:
  description: "Generates marketing strategies based on research."

campaign_idea_task:
  description: "Creates marketing campaign ideas."

copy_creation_task:
  description: "Writes promotional content."
```

## Running the Project
Run the AI-powered marketing assistant:
```bash
python src/main.py
```

## Logging
Logs are stored in the `logs/` directory. Adjust log levels in `logger.py`.

## License
This project is licensed under the MIT License.

## Contact
For issues or contributions, create a GitHub issue or contact the developer at [shahbazzulfiqar894@gmail.com].

