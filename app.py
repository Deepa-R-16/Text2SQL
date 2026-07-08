from sql_generator import generate_sql
from database import execute_query
from answer_generator import generate_answer
import pandas as pd


question = input("Ask your database question: ")

sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)

result = execute_query(sql)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("\nResult:")
print(result.head(20))

answer = generate_answer(question, result)

print("\nAI Answer:")
print(answer)

result.to_csv("query_result.csv", index=False)

print("\nFull result saved to query_result.csv")