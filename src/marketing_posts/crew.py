from typing import List
import os
import yaml
from pydantic import BaseModel
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import openai  # Import OpenAI API client
from logger import setup_logger

# Load environment variables
load_dotenv()

# Ensure API keys are loaded
serper_api_key = os.getenv("SERPER_API_KEY")
if not serper_api_key:
    raise ValueError("SERPER_API_KEY is missing in the environment variables")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is missing in the environment variables")

# Set OpenAI API key
openai.api_key = api_key

# Model used
llm_model = "gpt-3.5-turbo"

# Initialize logger
logger = setup_logger(__name__)

# Define SerperDevTool instance with API key
search_tool = SerperDevTool(
    api_key=serper_api_key,
    search_url="https://google.serper.dev/scholar",
    n_results=2,
)

scrape_tool = ScrapeWebsiteTool()

# Define Pydantic models
class MarketStrategy(BaseModel):
    name: str
    tactics: List[str]
    channels: List[str]
    kpis: List[str]

class CampaignIdea(BaseModel):
    name: str
    description: str
    audience: str
    channel: str

class Copy(BaseModel):
    title: str
    body: str

@CrewBase
class MarketingPostCrew:
    def __init__(self, agents_config_path=None, tasks_config_path=None):
        super().__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.agents_config_path = agents_config_path or os.path.join(base_dir, "config", "agents.yaml")
        self.tasks_config_path = tasks_config_path or os.path.join(base_dir, "config", "tasks.yaml")
        
        self.agents_config = self._load_config(self.agents_config_path)
        self.tasks_config = self._load_config(self.tasks_config_path)
        logger.info(f"Loaded configs: {self.agents_config_path}, {self.tasks_config_path}")

    def _load_config(self, config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    @agent
    def lead_market_analyst(self) -> Agent:
        return Agent(
            **self.agents_config.get("lead_market_analyst", {}),
            tools=[search_tool, scrape_tool],
            verbose=True
        )

    @agent
    def chief_marketing_strategist(self) -> Agent:
        return Agent(
            **self.agents_config.get("chief_marketing_strategist", {}),
            tools=[search_tool, scrape_tool],
            verbose=True
        )

    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            **self.agents_config.get("creative_content_creator", {}),
            verbose=True
        )

    @task
    def project_understanding_task(self) -> Task:
        return Task(
            **self.tasks_config.get("research_task", {}),
            agent=self.lead_market_analyst(),
            expected_output=str  # Use type, not string representation
        )

    @task
    def marketing_strategy_task(self) -> Task:
        return Task(
            **self.tasks_config.get("marketing_strategy_task", {}),
            agent=self.chief_marketing_strategist(),
            output_json=MarketStrategy,
            expected_output=MarketStrategy,  # Correct type instead of "MarketStrategy"
        )

    @task
    def campaign_idea_task(self) -> Task:
        return Task(
            **self.tasks_config.get("campaign_idea_task", {}),
            agent=self.creative_content_creator(),
            output_json=CampaignIdea,
            expected_output=CampaignIdea,  # Correct type instead of "CampaignIdea"
        )

    @task
    def copy_creation_task(self) -> Task:
        return Task(
            **self.tasks_config.get("copy_creation_task", {}),
            agent=self.creative_content_creator(),
            context=[self.marketing_strategy_task, self.campaign_idea_task],  # Correct reference
            output_json=Copy,
            expected_output=Copy,  # Correct type instead of "Copy"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.lead_market_analyst(), self.chief_marketing_strategist(), self.creative_content_creator()],
            tasks=[
                self.project_understanding_task(),
                self.marketing_strategy_task(),
                self.campaign_idea_task(),
                self.copy_creation_task(),
            ],
            process=Process.sequential,
            verbose=True
        )
