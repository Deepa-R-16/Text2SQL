from vector_search import search_similar
from langchain_community.agent_toolkits import create_sql_agent
from chat_memory import save_chat, get_chat_history
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Database connection
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

print("Database Connected!")

# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

# SQL Agent
agent = create_sql_agent(
    llm,
    db=db,
    verbose=False,
    max_iterations=10,
    early_stopping_method="generate"
)

while True:

    question = input("\nAsk your question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Load previous conversation
    history = get_chat_history()

    context = search_similar(question)

    history_text = ""

    context_text = "\n".join(context)

    for message in history:
        if message.type == "human":
            history_text += f"User: {message.content}\n"
        elif message.type == "ai":
            history_text += f"AI: {message.content}\n"

    print("\n------ Chat History ------")
    print(history_text)
    print("--------------------------")

    print("\nRelevant Context:")
    print(context_text)

    try:
        prompt = f"""
Relevant Database Information:
{context_text}

Previous Conversation:
{history_text}

Current Question:
{question}
"""

        response = agent.invoke(prompt)

        answer = response["output"]

        save_chat(question, answer)

        print("\nAI Answer:")
        print(answer)

    except Exception as e:
        print("\nError:")
        print(e)