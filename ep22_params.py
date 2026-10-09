# Episode 22: Parameters
# Step By Step Coding · Python basics
#
# Try it: Call greet with your own name and a greeting, then Run
# Then: Add print(power(5)) and print(power(5, 3)), then Run
# ---------------------------------------------

def greet(name, greeting="Hello"):
    print(greeting + ", " + name)
greet("Maya")
greet("Sam", "Hi")
greet(greeting="Hey", name="Lee")
def power(base, exp=2):
    return base ** exp
print(power(3))
print(power(2, 10))
