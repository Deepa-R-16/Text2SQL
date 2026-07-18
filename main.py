from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import time
from pydantic import BaseModel
from sql_generator import generate_sql
from database import execute_query
from answer_generator import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Text-to-SQL Backend is Running!"}
@app.get("/stats")
def get_stats():

    users = execute_query(
        "SELECT COUNT(*) AS count FROM users"
    ).iloc[0]["count"]

    products = execute_query(
        "SELECT COUNT(*) AS count FROM products"
    ).iloc[0]["count"]

    orders = execute_query(
        "SELECT COUNT(*) AS count FROM orders"
    ).iloc[0]["count"]

    return {
        "users": int(users),
        "products": int(products),
        "orders": int(orders)
    }


@app.post("/ask")
def ask_database(request: QueryRequest):

    question = request.question

    sql = generate_sql(question)

    sql = sql.replace("```sql", "").replace("```", "").strip()


    forbidden_keywords = [
        "DELETE",
        "UPDATE",
        "INSERT",
        "DROP",
        "ALTER",
        "TRUNCATE"
    ]


    for word in forbidden_keywords:
        if word in sql.upper():
            return {
                "question": question,
                "generated_sql": sql,
                "result": [],
                "rows": 0,
                "execution_time": 0,
                "ai_answer": "Only SELECT queries are allowed."
            }


    start = time.time()


    try:

        result = execute_query(sql)

    except Exception as e:

        return {
            "question": question,
            "generated_sql": sql,
            "result": [],
            "rows": 0,
            "execution_time": 0,
            "ai_answer": str(e)
        }


    answer = generate_answer(question, result)


    end = time.time()


    return {
        "question": question,
        "generated_sql": sql,
        "result": result.to_dict(orient="records"),
        "rows": len(result),
        "execution_time": round(end-start,3),
        "ai_answer": answer
    }