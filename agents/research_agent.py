# /agents/research_agent.py
import logging # ADDED
from typing import List, Dict
from .base_agent import BaseAgent
from tools.search import SearchTool
from tools.scraper import ScraperTool

class ResearchAgent(BaseAgent):
    """Searches the web and scrapes content."""
    def run(self, topic: str) -> List[Dict[str, str]]:
        search_tool = SearchTool()
        scraper_tool = ScraperTool()

        logging.info(f"ResearchAgent: Starting search for '{topic}'...")
        search_results = search_tool.search(query=topic)
        
        # ADDED: Log the search results
        if not search_results:
            logging.warning("ResearchAgent: Serper search returned no results.")
            return []
        
        logging.info(f"ResearchAgent: Found {len(search_results)} potential sources.")

        scraped_content = []
        for result in search_results:
            link = result.get('link')
            if not link:
                continue
            
            logging.info(f"ResearchAgent: Attempting to scrape {link}...")
            content = scraper_tool.scrape(link)
            
            if content.startswith("Error"):
                # ADDED: Log scraping errors
                logging.warning(f"ResearchAgent: Failed to scrape {link}. Reason: {content}")
            else:
                logging.info(f"ResearchAgent: Successfully scraped {link}.")
                scraped_content.append({"url": link, "content": content})
        
        if not scraped_content:
            logging.error("ResearchAgent: Scraping failed for all sources.")

        return scraped_content