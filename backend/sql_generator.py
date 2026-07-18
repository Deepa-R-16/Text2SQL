from schema import get_schema
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY FOUND:", api_key is not None)
print("API KEY VALUE:", repr(api_key))

client = genai.Client(api_key=api_key)

def generate_sql(question):

    schema = get_schema()

    prompt = f"""
You are an expert PostgreSQL SQL developer.

Use the following database schema:

{schema}

Convert the user's natural language question into SQL.

Rules:
- Return only SQL query.
- Do not add explanation.
- Use PostgreSQL syntax.
- Use correct table relationships when required.

User question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

if __name__ == "__main__":

    question = "Show all orders with customer names"

    sql_query = generate_sql(question)

    print("Generated SQL:")
    print(sql_query)