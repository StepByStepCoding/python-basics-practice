# Episode 15: while, break and continue
# Step By Step Coding · Python basics
#
# Try it: Change the 3 to a 5 and press Run
# Then: Change 20 to 50 in the last loop. What is total? Press Run
# ---------------------------------------------

count = 0
while True:
    count = count + 1
    print(count)
    if count == 3:
        break
for n in range(1, 6):
    if n == 3:
        continue
    print(n)
total = 0
for n in range(1, 100):
    total = total + n
    if total > 20:
        break
print(total)
