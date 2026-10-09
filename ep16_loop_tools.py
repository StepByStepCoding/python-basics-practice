# Episode 16: range, enumerate and zip
# Step By Step Coding · Python basics
#
# Try it: Change the step 3 to 2 and press Run
# Then: Use enumerate(names, 1) to start counting at 1, then Run
# ---------------------------------------------

for i in range(2, 10, 3):
    print(i)
names = ["Maya", "Sam", "Lee"]
scores = [90, 72, 85]
for i, n in enumerate(names):
    print(i, n)
for n, s in zip(names, scores):
    print(n, s)
for i in range(3, 0, -1):
    print(i)
