# /workflow/orchestrator.py
import logging
from agents.knowledge_agent import KnowledgeAgent
from agents.research_agent import ResearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.report_agent import ReportAgent

class Orchestrator:
    """Manages the entire research workflow."""
    def __init__(self):
        self.knowledge_agent = KnowledgeAgent()
        self.research_agent = ResearchAgent()
        self.summarizer_agent = SummarizerAgent()
        self.analyzer_agent = AnalyzerAgent()
        self.report_agent = ReportAgent()

    def run(self, topic: str) -> str:
        logging.info(f"Orchestrator: Starting research for '{topic}'")

        logging.info("Step 1: Getting background info...")
        background = self.knowledge_agent.run(topic)
        
        logging.info("Step 2: Finding and scraping sources...")
        scraped_data = self.research_agent.run(topic)
        if not scraped_data:
            return "Could not find sufficient information for a report."
        
        logging.info(f"Step 3: Summarizing {len(scraped_data)} sources...")
        summaries = [self.summarizer_agent.run(content=item['content'], url=item['url']) for item in scraped_data]
        
        logging.info("Step 4: Analyzing findings...")
        analysis = self.analyzer_agent.run(topic=topic, summaries=summaries)
        
        logging.info("Step 5: Generating final report...")
        final_report = self.report_agent.run(topic=topic, background=background, summaries=summaries, analysis=analysis)
        
        logging.info("Orchestrator: Process complete.")
        return final_report
