


def negative_testcase_prompt(requirement):
    prompt = f""" 
    You are a Senior QA Engineer 
    Analyze the given requirement and generate negative test cases in the specified format.
    Each test case must contain:
    - Test Case ID
    - Description
    - Priority
    - Pre-requisite
    - Steps
    - Expected Result 
    Generate exactly 10 test cases:
    - P1: 4 test cases
    - P2: 3 test cases
    - P3: 3 test cases
    Cover only negative test scenarios relevant to the given requirement.
    - Negative
    Generate negative scenarios based on the given requirement.
    Do not assume unrelated features that are not mentioned in the requirement.
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