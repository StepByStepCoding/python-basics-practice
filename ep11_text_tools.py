# Episode 11: String methods
# Step By Step Coding · Python basics
#
# Try it: Replace "World" with your own name, then press Run
# Then: Add print(clean.upper()) and print(clean.count("l")), then Run
# ---------------------------------------------

text = "  Hello, World  "
clean = text.strip()
print(clean)
print(clean.lower())
print(clean.replace("World", "Python"))
print(clean.split(", "))
print(clean.startswith("Hello"))
print("World" in clean)
print(clean.find("World"))
