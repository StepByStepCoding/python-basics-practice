# Episode 6: Lists and dictionaries
# Step By Step Coding · Python basics
#
# Try it: Add scores.append(100) and press Run
# Then: Add person["city"] = "Atlanta" and print(person), then Run
# ---------------------------------------------

scores = [90, 72, 85]
print(scores[0])
scores.append(60)
print(len(scores))
for s in scores:
    print(s)
person = {"name": "Maya"}
print(person["name"])
person["age"] = 30
