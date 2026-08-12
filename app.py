from providers.claude_provider import ClaudeProvider
from services.testcase_service import TestCaseService
from utils.file_utils import save_testcase
from providers.openai_provider import OpenAIProvider

def main():
    print("Welcome to TestPilot AI")
    requirement = "User should be able to login using username and password"
    ai_provider = input("Select AI provider (claude/openai): ").lower()
    try:
        if ai_provider == "claude":
            provider = ClaudeProvider()
        elif ai_provider == "openai":
            provider = OpenAIProvider()
        else:
            raise ValueError("Invalid ai_provider")
        obj = TestCaseService(provider)
        response = obj.generate_testcases(requirement)
        filename = f"{ai_provider}_testcases.txt"
        save_testcase(filename,response)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

