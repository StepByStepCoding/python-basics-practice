# Episode 5: Loops
# Step By Step Coding · Python basics
#
# Try it: Change range(3) to range(6), then press Run
# Then: Change range(1, 6) to range(1, 11). What will total be? Press Run
# ---------------------------------------------

for i in range(3):
    print(i)
total = 0
for i in range(1, 6):
    total = total + i
print(total)
for letter in "Maya":
    print(letter)
count = 0
while count < 3:
    print("Loop", count)
    count = count + 1
