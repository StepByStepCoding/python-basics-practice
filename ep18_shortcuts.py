# Episode 18: List comprehensions
# Step By Step Coding · Python basics
#
# Try it: Change n * n to n * 3 and press Run
# Then: Add print([len(w) for w in words]) and press Run
# ---------------------------------------------

nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print(squares)
evens = [n for n in nums if n % 2 == 0]
print(evens)
words = ["python", "ai", "code"]
upper = [w.upper() for w in words]
print(upper)
