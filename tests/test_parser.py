from src.parser import *
# x = parse_query("busch double")
# print(x)
# y = query_to_vector(x)
# print(y)

# z = search({"AC": "Yes", "Campus": "Busch"}, 999)
z = search_nlp("private", 30)

print(z)
