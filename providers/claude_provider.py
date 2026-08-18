from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

class ClaudeProvider:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key)

    def get_response(self, prompt,schema=None):
            if not prompt or not prompt.strip():
                raise ValueError("Prompt cannot be empty")
            data = [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            request_params = {
                "model": "claude-sonnet-5",
                "system": """You are a Senior QA Engineer.
            Do not invent or assume any functionality that is not explicitly mentioned in the requirement.""",
                "messages": data,
                "max_tokens": 5000,
                "temperature": 1.0
            }
            if schema is not None:
                request_params['output_config'] = {
                    "format": {
                        "type": "json_schema",
                        "schema": schema
                    }
                }
            response = self.client.messages.create(**request_params)
            for block in response.content:
                if block.type == "text":
                    if not block.text:
                        raise ValueError("Response text is empty")
                    return block.text
            raise ValueError("No text response received from Claude")