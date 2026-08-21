



def build_code_generation_prompt(test_case, framework_context):
    return f"""Generate Python pytest automation code for the given test case requirement.
Follow the existing framework context and conventions.
Do not invent framework methods or fixtures.
Return only executable Python code.

TEST CASE:
{test_case}

FRAMEWORK CONTEXT:
{framework_context}"""

