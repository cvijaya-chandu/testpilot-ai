TESTCASE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "description": {"type": "string"},
        "priority": {"type": "string"},
        "pre_requisite": {"type": "string"},
        "steps": {
            "type": "array",
            "items": {"type": "string"}
        },
        "expected_result": {"type": "string"}
    },
    "required": [
        "id",
        "description",
        "priority",
        "pre_requisite",
        "steps",
        "expected_result"
    ],
    "additionalProperties": False
}
TESTCASES_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "test_cases": {
            "type": "array",
            "items": TESTCASE_SCHEMA
        }
    },
    "required": ["test_cases"],
    "additionalProperties": False
}