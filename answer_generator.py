from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question, result):

    prompt = f"""
You are a data analyst.

User question:
{question}

Database result:
{result}

Explain the result clearly in a short answer.
Mention important insights if available.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text