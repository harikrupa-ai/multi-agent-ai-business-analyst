from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def suggest_architecture(requirements: str) -> str:
    prompt = f"""
You are a Senior Solutions Architect.

Suggest a practical system architecture for the following software requirements.

Requirements:
{requirements}

Return:
1. Recommended architecture
2. Frontend technology
3. Backend technology
4. Database
5. APIs/integrations
6. Security considerations
7. Deployment recommendation
"""
    response = llm.invoke(prompt)
    return response.content