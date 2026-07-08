import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

# User enters SQL
query = input("Enter SQL Query: ")

cursor.execute(query)

rows = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]

df = pd.DataFrame(rows, columns=columns)

print(df)

cursor.close()
connection.close()