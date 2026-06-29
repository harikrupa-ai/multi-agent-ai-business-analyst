from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def generate_user_stories(requirements: str) -> str:
    prompt = f"""
You are an Agile Product Owner.

Convert the following requirements into user stories.

Requirements:
{requirements}

Return:
1. Epics
2. User Stories in format:
   As a [user],
   I want [goal],
   So that [benefit].
3. Acceptance Criteria for each story.
"""
    response = llm.invoke(prompt)
    return response.content