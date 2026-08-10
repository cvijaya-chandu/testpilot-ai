from providers.claude_provider import ClaudeProvider



class TestCaseService:
    def __init__(self):
        self.claude_provider = ClaudeProvider()

    def generate_testcases(self,requirement):
        prompt = "You are a QA engineer. Generate test cases for the following requirement: " + requirement
        response = self.claude_provider.generate(prompt)
        return response
