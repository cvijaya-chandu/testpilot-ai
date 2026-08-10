from providers.claude_provider import ClaudeProvider
from services.testcase_service import TestCaseService

def main():
    print("Welcome to TestPilot AI")
    # obj = ClaudeProvider()
    # response = obj.generate("Explain about Python")
    requirement = "User should be able to login using username and password"
    obj = TestCaseService()
    response = obj.generate_testcases(requirement)
    print(response.content[0].text)

if __name__ == "__main__":
    main()

