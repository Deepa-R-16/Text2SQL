from vector_search import search_similar

query = "Where are customer details stored?"

results = search_similar(query)

print("Relevant Documents:")

for doc in results:
    print("-", doc)