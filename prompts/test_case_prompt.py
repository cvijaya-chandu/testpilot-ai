def build_testcase_prompt(requirement):
    prompt = f""" 
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
    Example Test Case-1:
    {{
    "id": "TC001",
    "description": "Verify login with valid username and password",
    "priority": "P1",
    "pre_requisite": "Valid user account exists",
    "steps": [
        "Enter valid username",
        "Enter valid password",
        "Click Login"
    ],
    "expected_result": "User should be able to login successfully"
}}
    Example Test Case-2:  
    {{
    "id": "TC002",
    "description": "Verify login with invalid username",
    "priority": "P1",
    "pre_requisite": "user account dont exists",
    "steps": [
        "Enter invalid username",
        "Enter password",
        "Click Login"
    ],
    "expected_result": "User should not be able to login successfully"
}}
    Example Test Case-3:  
    {{
    "id": "TC003",
    "description": "Verify login with invalid password",
    "priority": "P1",
    "pre_requisite": "user account exists",
    "steps": [
        "Enter valid username",
        "Enter invalid password",
        "Click Login"
    ],
    "expected_result": "User should not be able to login successfully"
}}
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
    return prompt