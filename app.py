from providers.claude_provider import ClaudeProvider
from services.testcase_service import TestCaseService
from utils.file_utils import save_testcase

def main():
    print("Welcome to TestPilot AI")
    filename = 'testcases.txt'
    requirement = "User should be able to login using username and password"
    try:
        obj = TestCaseService()
        response = obj.generate_testcases(requirement)
        save_testcase(filename,response)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

