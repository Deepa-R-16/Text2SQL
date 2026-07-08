from chat_memory import save_chat, get_chat_history
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from dotenv import load_dotenv
import os

load_dotenv()

# Database connection
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

print("Database connected through LangChain")


# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

# Create SQL agent
agent = create_sql_agent(
    llm,
    db=db,
    verbose=False,
    max_iterations=10,
    early_stopping_method="generate"
)

while True:
    question = input("\nAsk your database question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = agent.invoke(question)
        save_chat(question, response["output"])
        print("\nAI Answer:")
        print(response["output"])

    except Exception as e:
        print("\nError:")
        print(e)