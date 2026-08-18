
from prompts.log_analysis_prompt import build_log_analysis_prompt

class LogAnalyzerService:
    def __init__(self, provider):
        self.provider = provider

    def analyze_log(self,failed_tests):
        prompt = build_log_analysis_prompt(failed_tests)
        response = self.provider.get_response(prompt)
        return response
