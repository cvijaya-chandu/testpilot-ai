from pydantic import BaseModel

class TestCase(BaseModel):
    id: str
    description: str
    priority: str
    pre_requisite: str
    steps: list[str]
    expected_result: str

class TestCasesResponse(BaseModel):
    test_cases: list[TestCase]