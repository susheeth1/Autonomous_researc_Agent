# /agents/knowledge_agent.py
from .base_agent import BaseAgent

class KnowledgeAgent(BaseAgent):
    """Provides background knowledge and definitions."""
    def run(self, topic: str) -> str:
        prompt = f"Provide a concise background and define key terms for the topic: \"{topic}\". Explain the foundational concepts simply."
        return self._create_chat_completion(prompt)
