import psycopg2
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

cursor.execute("""
SELECT
    table_name,
    column_name,
    data_type
FROM information_schema.columns
WHERE table_schema='public'
ORDER BY table_name, ordinal_position;
""")

rows = cursor.fetchall()

current_table = ""

for table, column, datatype in rows:

    if table != current_table:
        current_table = table
        print(f"\nTable: {table}")
        print("-" * 30)

    print(f"{column} ({datatype})")

cursor.close()
connection.close()