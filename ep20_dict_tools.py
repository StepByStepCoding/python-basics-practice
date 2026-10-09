# Episode 20: Dictionaries in depth
# Step By Step Coding · Python basics
#
# Try it: Add person["pet"] = "dog" and press Run
# Then: Count the letters in your own name with counts, then Run
# ---------------------------------------------

person = {"name": "Maya", "age": 30}
print(person.get("city", "unknown"))
person["city"] = "Atlanta"
for key, value in person.items():
    print(key, value)
del person["age"]
print("name" in person)
counts = {}
for w in ["a", "b", "a"]:
    counts[w] = counts.get(w, 0) + 1
print(counts)
