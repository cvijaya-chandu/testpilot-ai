from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

class ClaudeProvider:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key)

    def generate(self, prompt):
        try:
            if not prompt or not prompt.strip():
                return f'prompt cannot be empty'
            else:
                messages = [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
                response = self.client.messages.create(model="claude-sonnet-5",messages=messages,max_tokens=1000)
                return response

        except Exception as e:
            raise