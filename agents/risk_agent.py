from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def analyze_risks(requirements: str) -> str:
    prompt = f"""
You are a Senior Risk Analyst.

Analyze the following software requirements and identify project risks.

Requirements:
{requirements}

Return:
1. Technical risks
2. Business risks
3. Security risks
4. Compliance risks
5. Mitigation strategies
"""
    response = llm.invoke(prompt)
    return response.content