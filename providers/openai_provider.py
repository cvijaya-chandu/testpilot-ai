import os

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()



class OpenAIProvider:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt):
            if not prompt or not prompt.strip():
                raise ValueError("Prompt cannot be empty")
            response = self.client.responses.create(model="gpt-5.6-luna",input=prompt,max_output_tokens=10000)
            if not response.output_text:
                raise ValueError("Response text is empty")
            return response.output_text
