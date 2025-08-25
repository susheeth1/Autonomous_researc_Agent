# /agents/report_agent.py
from typing import List
from .base_agent import BaseAgent

class ReportAgent(BaseAgent):
    """Generates the final structured report."""
    def run(self, topic: str, background: str, summaries: List[str], analysis: str) -> str:
        summaries_str = "\n\n".join(summaries)
        prompt = f"Generate a comprehensive research report in Markdown on \"{topic}\". Use the provided components for each section: Introduction (background), Key Findings (summaries), Analysis (synthesis), and a Conclusion.\n\nBACKGROUND:\n---\n{background}\n---\n\nSUMMARIES:\n---\n{summaries_str}\n---\n\nANALYSIS:\n---\n{analysis}\n---"
        return self._create_chat_completion(prompt)
