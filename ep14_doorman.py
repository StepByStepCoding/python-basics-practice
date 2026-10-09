# Episode 14: Nested decisions
# Step By Step Coding · Python basics
#
# Try it: Set has_ticket to False and press Run
# Then: Change age to 16. Which branch runs? Press Run
# ---------------------------------------------

age = 20
has_ticket = True
if age >= 18:
    if has_ticket:
        print("Welcome in")
    else:
        print("Buy a ticket")
else:
    print("Too young")
day = "sat"
if day in ["sat", "sun"]:
    print("Weekend")
else:
    print("Weekday")
status = "adult" if age >= 18 else "minor"
print(status)
