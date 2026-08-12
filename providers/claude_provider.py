from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

class ClaudeProvider:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key)

    def generate(self, prompt):
            if not prompt or not prompt.strip():
                raise ValueError("Prompt cannot be empty")
            messages = [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            response = self.client.messages.create(model="claude-sonnet-5",messages=messages,max_tokens=5000)
            for block in response.content:
                if block.type == "text":
                    if not block.text:
                        raise ValueError("Response text is empty")
                    return block.text
            raise ValueError("No text response received from Claude")