def build_testcase_prompt(requirement):
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
    return prompt