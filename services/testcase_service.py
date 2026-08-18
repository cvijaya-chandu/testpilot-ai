import json
from prompts.test_case_prompt import build_testcase_prompt
from prompts.requirement_analysis_prompt import build_requirement_analysis_prompt
from prompts.negative_test_prompt import negative_testcase_prompt
from models.testcase_model import TestCasesResponse
from pydantic import ValidationError
from models.testcase_schema import TESTCASES_RESPONSE_SCHEMA
class TestCaseService:
    def __init__(self,provider):
        self.provider = provider

    def generate_testcases(self,requirement):
        prompt = build_testcase_prompt(requirement)
        if not requirement or not requirement.strip():
            raise ValueError("Requirement is mandatory")
        response = self.provider.get_response(
            prompt,
            TESTCASES_RESPONSE_SCHEMA
        )
        print(response)
        response_json = json.loads(response)
        try:
            validated_response = TestCasesResponse.model_validate(response_json)
        except ValidationError as e:
            print(f"Response validation failed: {e}")
            raise
        self.validate_testcases(response_json)
        return response_json

    def analyze_requirement(self, requirement):
        if not requirement or not requirement.strip():
            raise ValueError("Requirement cannot be empty")
        prompt = build_requirement_analysis_prompt(requirement)
        response = self.provider.get_response(prompt)
        response_json = json.loads(response)
        return response_json

    def generate_negative_testcases(self, requirement):
        if not requirement or not requirement.strip():
            raise ValueError("Requirement cannot be empty")
        prompt = negative_testcase_prompt(requirement)
        response = self.provider.get_response(prompt)
        response_json = json.loads(response)
        return response_json

    def validate_testcases(self, data):
        if 'test_cases' not in data:
            raise ValueError("No test cases provided")
        if len(data["test_cases"]) != 15:
            raise ValueError("Expected 15 test cases")
        for i in data["test_cases"]:
            if 'id' not in i:
                raise ValueError("Test case id is mandatory")
        if len(i['id']) == 0:
            raise ValueError("Test case id is mandatory")
        d = ['id', 'description', 'priority', 'pre_requisite', 'steps', 'expected_result']
        p = {}
        for i in data["test_cases"]:
            for key in d:
                if key not in i:
                    raise ValueError(f"{key} is mandatory")

                if i[key] == "":
                    raise ValueError(f"{key} value is empty")

            if i['priority'] not in ["P1","P2","P3"]:
                raise ValueError(f"Priority should be P1 or P2 or P3")

            if i['priority'] in p:
                p[i['priority']] = p[i['priority']] + 1
            else:
                p[i["priority"]] = 1
        #
        #
        # if p['P1'] != 5:
        #     raise ValueError(f"P1 cases should be 5")
        # if p['P2'] != 7:
        #     raise ValueError(f"P2 cases should be 7")
        # if p['P3'] != 3:
        #     raise ValueError(f"P3 cases should be 3")






