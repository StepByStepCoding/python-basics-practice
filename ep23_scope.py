# Episode 23: Scope and return values
# Step By Step Coding · Python basics
#
# Try it: Change the 5 inside change() to 99. Does outside change? Run
# Then: Add print(min_max([7, 1, 9])) and press Run
# ---------------------------------------------

x = 10
def change():
    x = 5
    print("inside", x)
change()
print("outside", x)
def min_max(nums):
    return min(nums), max(nums)
low, high = min_max([4, 9, 2])
print(low, high)
def shout(text):
    print(text.upper())
result = shout("hi")
print(result)
