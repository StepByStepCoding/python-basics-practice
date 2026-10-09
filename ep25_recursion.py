# Episode 25: Recursion
# Step By Step Coding · Python basics
#
# Try it: Change countdown(3) to countdown(5) and press Run
# Then: Add print(factorial(6)) and press Run
# ---------------------------------------------

def countdown(n):
    if n == 0:
        print("Go!")
    else:
        print(n)
        countdown(n - 1)
countdown(3)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(6))
