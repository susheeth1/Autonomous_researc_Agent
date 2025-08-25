# /agents/base_agent.py
import os
import logging
from abc import ABC, abstractmethod
from openai import OpenAI, NotFoundError

class BaseAgent(ABC):
    """Abstract base class for agents with future-proof model selection."""
    def __init__(self):
        self.primary_model = "gpt-5-nano"
        self.fallback_model = "gpt-4o-mini"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def _create_chat_completion(self, prompt: str) -> str:
        """Creates a chat completion, trying the primary model first."""
        try:
            response = self.client.chat.completions.create(
                model=self.primary_model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content or "No content returned."
        except NotFoundError:
            logging.warning(f"Model '{self.primary_model}' not found. Falling back to '{self.fallback_model}'.")
            try:
                response = self.client.chat.completions.create(
                    model=self.fallback_model,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.choices[0].message.content or "No content returned."
            except Exception as e:
                return f"Error with fallback model: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
