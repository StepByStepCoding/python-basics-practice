# Episode 4: Conditions
# Step By Step Coding · Python basics
#
# Try it: Change age to 18, then to 17. Press Run each time
# Then: Set has_ticket to False. Predict the output, then press Run
# ---------------------------------------------

age = 20
if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")
score = 72
if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Keep going")
has_ticket = True
if age >= 18 and has_ticket:
    print("Welcome in")
if age == 20:
    print("Exactly twenty")
