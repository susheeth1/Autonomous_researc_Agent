# /agents/analyzer_agent.py
from typing import List
from .base_agent import BaseAgent

class AnalyzerAgent(BaseAgent):
    """Compares findings and extracts insights."""
    def run(self, topic: str, summaries: List[str]) -> str:
        summaries_str = "\n\n".join(summaries)
        prompt = f"As a research analyst, analyze these summaries on \"{topic}\". Identify key themes, compare viewpoints, and synthesize the main insights.\n\nSUMMARIES:\n---\n{summaries_str}\n---"
        return self._create_chat_completion(prompt)
