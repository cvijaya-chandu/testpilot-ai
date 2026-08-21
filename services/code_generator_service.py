
from prompts.code_generation_prompt import build_code_generation_prompt


class CodeGeneratorService:
    def __init__(self, provider):
        self.provider = provider

    def generate_testcase_code(self, test_case,framework_context):
        prompt = build_code_generation_prompt(test_case,framework_context)
        response = self.provider.get_response(prompt)
        return response