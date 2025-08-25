# /tools/scraper.py
import requests
from bs4 import BeautifulSoup

class ScraperTool:
    """A tool to scrape text content from a URL."""
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    def scrape(self, url: str, max_chars: int = 4000) -> str:
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            for script_or_style in soup(['script', 'style']):
                script_or_style.decompose()
            
            text = '\n'.join(line.strip() for line in soup.get_text().splitlines() if line.strip())
            return text[:max_chars]
        except requests.RequestException as e:
            return f"Error scraping URL {url}: {e}"
