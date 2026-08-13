


def build_requirement_analysis_prompt(requirement):
    prompt = f"""
    You are an experienced Software Test Engineer.
    Analyze the following requirement from a testing perspective.
    Identify:
    1. Missing information
    2. Ambiguous requirements
    3. Potential testing risks
    4. Questions that should be clarified before testing
    Return only valid JSON.
    Do not include markdown code fences, backticks, or the word json outside the JSON object.
    Use the following JSON keys:
    - requirement
    - requirement_analysis
    - missing_information
    - ambiguous_requirements
    - potential_testing_risks
    - clarifying_questions
    Requirement:
    {requirement}
    """
    return prompt