
from prompts.eval_prompt import build_eval_prompt

class EvalService:
    def __init__(self, provider):
        self.provider = provider

    def evaluate(self, requirement, generated_testcases):
        prompt = build_eval_prompt(requirement, generated_testcases)
        evaluation = self.provider.get_response(prompt)
        return evaluation
