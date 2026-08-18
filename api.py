from fastapi import FastAPI
from services.testcase_service import TestCaseService
from services.log_analyzer_service import LogAnalyzerService
from providers.claude_provider import ClaudeProvider
from pydantic import BaseModel

app = FastAPI()
provider = ClaudeProvider()
service = TestCaseService(provider)
logservice = LogAnalyzerService(provider)

class TestCaseRequest(BaseModel):
    requirement: str

class LogRequest(BaseModel):
    logs: list[dict]

@app.get("/health")
def health_check():
    return {"status": "TestPilot Working"}

@app.post("/generate-testcases")
def generate_testcase(input_data: TestCaseRequest):
    response = service.generate_testcases(input_data.requirement)
    return response

@app.post("/analyze-logs")
def analyze_logs(input_data: LogRequest):
    response = logservice.analyze_log(input_data.logs)
    return response
