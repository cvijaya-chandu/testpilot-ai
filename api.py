from fastapi import FastAPI
from services.testcase_service import TestCaseService
from services.log_analyzer_service import LogAnalyzerService
from services.code_generator_service import CodeGeneratorService
from providers.claude_provider import ClaudeProvider
from pydantic import BaseModel

app = FastAPI()
provider = ClaudeProvider()
service = TestCaseService(provider)
logservice = LogAnalyzerService(provider)
codeservice = CodeGeneratorService(provider)

class TestCaseRequest(BaseModel):
    requirement: str

class LogRequest(BaseModel):
    logs: list[dict]

class CodeRequest(BaseModel):
    test_case: str
    context:str


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

@app.post("/generate-code")
def generate_testcase_code(input_data: CodeRequest):
    response = codeservice.generate_testcase_code(
        input_data.test_case,
        input_data.context)
    return response

