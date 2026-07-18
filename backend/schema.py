import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


def get_schema():

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
        WHERE table_schema='public';
    """)

    rows = cursor.fetchall()

    schema = ""

    for table, column, datatype in rows:
        schema += f"{table}({column}: {datatype})\n"

    cursor.close()
    connection.close()

    return schema


if __name__ == "__main__":
    print(get_schema())