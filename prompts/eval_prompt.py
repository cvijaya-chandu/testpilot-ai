def build_eval_prompt(requirement, generated_testcases):
    return f"""
Evaluate the generated test cases against the given requirement.

Requirement:
{requirement}

Generated Test Cases:
{generated_testcases}

Evaluation criteria:
1. Relevance - Are the test cases relevant to the requirement?
2. Coverage - Do the test cases cover the requirement adequately?
3. Groundedness - Do the test cases avoid unsupported assumptions?
4. Duplication - Are the test cases meaningfully different?

Give each criterion a score from 1 to 5.
"""