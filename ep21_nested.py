# Episode 21: Nested data
# Step By Step Coding · Python basics
#
# Try it: Add your own skill with append, then press Run
# Then: Print the second user: users[1]["name"], then press Run
# ---------------------------------------------

user = {
    "name": "Maya",
    "skills": ["python", "sql"],
    "address": {"city": "Atlanta"}
}
print(user["skills"][0])
print(user["address"]["city"])
user["skills"].append("ai")
users = [
    {"name": "Maya", "age": 30},
    {"name": "Sam", "age": 25}
]
for u in users:
    print(u["name"])
names = [u["name"] for u in users]
total = sum([u["age"] for u in users])
