# /agents/summarizer_agent.py
from .base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    """Summarizes text content."""
    def run(self, content: str, url: str) -> str:
        prompt = f"Summarize the key facts and findings from the following text (from URL {url}) as concise bullet points.\n\nCONTENT:\n---\n{content}\n---"
        return self._create_chat_completion(prompt)
