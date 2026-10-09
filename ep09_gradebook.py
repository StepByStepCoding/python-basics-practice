# Episode 9: Mini project
# Step By Step Coding · Python basics
#
# Try it: Change one of the scores and press Run. Watch avg
# Then: Change the pass mark from 80 to 75, then press Run
# When it asks you to type something, try: Maya (or your own answers)
# ---------------------------------------------

def average(nums):
    return round(sum(nums) / len(nums), 1)
scores = [90, 72, 85]
avg = average(scores)
name = input("Student name? ")
for s in scores:
    if s >= 80:
        print(s, "pass")
    else:
        print(s, "try again")
print(f"{name}'s average is {avg}")
