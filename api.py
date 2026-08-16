from fastapi import FastAPI
from services.testcase_service import TestCaseService
from providers.claude_provider import ClaudeProvider
from pydantic import BaseModel

app = FastAPI()
provider = ClaudeProvider()
service = TestCaseService(provider)

class TestCaseRequest(BaseModel):
    requirement: str

@app.get("/health")
def health_check():
    return {"status": "TestPilot Working"}

@app.post("/generate-testcases")
def generate_testcase(input_data: TestCaseRequest):
    response = service.generate_testcases(input_data.requirement)
    return response
