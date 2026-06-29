from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def gather_requirements(user_request: str) -> str:
    prompt = f"""
    You are a Senior Business Analyst.

    Analyze this stakeholder request:

    {user_request}

    Return:
    1. Summary
    2. Functional Requirements
    3. Non-Functional Requirements
    4. User Stories
    5. Risks / Gaps
    6. Follow-up Questions
    """
    response = llm.invoke(prompt)
    return response.content