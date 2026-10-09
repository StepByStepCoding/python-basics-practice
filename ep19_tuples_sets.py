# Episode 19: Tuples and sets
# Step By Step Coding · Python basics
#
# Try it: Change the point to (10, 20) and press Run
# Then: Make your own list with repeats and dedupe it with set()
# ---------------------------------------------

point = (3, 4)
x, y = point
print(x, y)
ids = {1, 2, 3, 2, 1}
print(len(ids))
ids.add(4)
print(sorted(ids))
nums = [1, 2, 2, 3, 3, 3]
unique = sorted(set(nums))
print(unique)
