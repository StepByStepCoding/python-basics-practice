# Episode 8: Errors
# Step By Step Coding · Python basics
#
# Try it: Change the 0 to a 5 and press Run. No error now
# Then: Run it and type 7. Then run again and type abc
# When it asks you to type something, try: abc (or your own answers)
# ---------------------------------------------

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Can't divide by zero")
text = input("Enter a number: ")
try:
    number = int(text)
    print("Thanks!")
except ValueError:
    print("That is not a number")
