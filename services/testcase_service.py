import json


class TestCaseService:
    def __init__(self,provider):
        self.provider = provider

    def generate_testcases(self,requirement):
        prompt = f""" 
        You are a Senior QA Engineer 
        Analyze the given requirement and generate test cases in the specified format.
        Each test case must contain:
        - Test Case ID
        - Description
        - Priority
        - Pre-requisite
        - Steps
        - Expected Result 
        Generate exactly 15 test cases:
        - P1: 5 test cases
        - P2: 6 test cases
        - P3: 4 test cases
        Cover all relevant test scenarios, including:
        - Positive
        - Negative
        - Boundary / Edge cases
        - Security
        - UI/UX
        - Performance
        Do not invent or assume any functionality that is not explicitly mentioned in the requirement.
        Return only valid JSON.
        Do not include markdown code fences, backticks, or the word json outside the JSON object.
        Use the following JSON keys:
        test_cases
        id
        description
        priority
        pre_requisite
        steps
        expected_result
        Requirement:
        {requirement}"""
        if not requirement or not requirement.strip():
            raise ValueError("Requirement is mandatory")
        response = self.provider.get_response(prompt)
        response_json = json.loads(response)
        self.validate_testcases(response_json)
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






