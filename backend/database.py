import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def execute_query(sql_query):

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    # Remove markdown formatting from Gemini output
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    cursor.execute(sql_query)

    results = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    df = pd.DataFrame(results, columns=columns)

    cursor.close()
    connection.close()

    return df