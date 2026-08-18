

def build_log_analysis_prompt(failed_tests):
    return f"""
You are analyzing failures from a pytest test execution.

Failed test information:
{failed_tests}

Analyze the failures and:
1. Group failures that appear to have the same root cause.
2. Identify the probable cause for each group.
3. Provide evidence from the supplied failure logs.
4. Suggest debugging steps.
5. Do not invent a cause if there is not enough evidence.
"""