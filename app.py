from providers.claude_provider import ClaudeProvider

def main():
    print("Welcome to TestPilot AI")
    obj = ClaudeProvider()
    response = obj.generate("Explain about Python")
    print(response.content[0].text)

if __name__ == "__main__":
    main()

