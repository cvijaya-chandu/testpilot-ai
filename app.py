

from providers.claude_provider import ClaudeProvider
from services.testcase_service import TestCaseService
from utils.file_utils import save_testcase
from providers.openai_provider import OpenAIProvider
from services.eval_service import EvalService

def main():
    print("Welcome to TestPilot AI")
    requirement = "User should be able to login using username and password"
    ai_provider = input("Select AI provider:(claude/openai): ").lower()
    try:
        if ai_provider == "claude":
            provider = ClaudeProvider()
        elif ai_provider == "openai":
            provider = OpenAIProvider()
        else:
            raise ValueError("Invalid ai_provider")
        obj = TestCaseService(provider)
        operation = input(
            "Select operation: (generate/analyze/negativetests): "
        ).strip().lower()
        if operation == "generate":
            response = obj.generate_testcases(requirement)
            eval_service = EvalService(provider)
            evaluation = eval_service.evaluate(requirement, response)
            print(evaluation)
        elif operation == "analyze":
            response = obj.analyze_requirement(requirement)
        elif operation == "negativetests":
            response = obj.generate_negative_testcases(requirement)
        else:
            print("Invalid operation")
        filename = f"{ai_provider}_testcases.csv"
        save_testcase(filename,response)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()