# /tools/search.py
import os
from serpapi import GoogleSearch
from typing import List, Dict

class SearchTool:
    """A tool to perform web searches using the Serper.dev API."""
    def __init__(self):
        self.api_key = os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise ValueError("SERPER_API_KEY environment variable not set.")

    def search(self, query: str, num_results: int = 5) -> List[Dict[str, str]]:
        params = {"engine": "google", "q": query, "api_key": self.api_key, "num": num_results}
        try:
            search = GoogleSearch(params)
            results = search.get_dict().get("organic_results", [])
            return [{"title": res.get("title"), "link": res.get("link"), "snippet": res.get("snippet")} for res in results]
        except Exception as e:
            print(f"Error during search: {e}")
            return []
