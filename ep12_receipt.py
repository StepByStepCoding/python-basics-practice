# Episode 12: Formatting output
# Step By Step Coding · Python basics
#
# Try it: Change qty to 5 and press Run
# Then: Print the price with three decimals using {price:.3f}, then Run
# ---------------------------------------------

name = "Maya"
price = 19.99
qty = 3
print(f"{name} bought {qty} items")
print(f"Total: ${price * qty:.2f}")
print("a", "b", "c", sep="-")
print("Loading", end="...")
print("done")
print(f"{name:>8}|")
