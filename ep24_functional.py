# Episode 24: lambda, map, filter and sorted
# Step By Step Coding · Python basics
#
# Try it: Sort names with key=lambda s: s[-1], then press Run
# Then: Sort nums by distance from 3: key=lambda n: abs(n - 3)
# ---------------------------------------------

nums = [3, 1, 4, 1, 5]
print(sorted(nums))
print(sorted(nums, reverse=True))
names = ["maya", "Sam", "lee"]
print(sorted(names, key=len))
is_even = lambda n: n % 2 == 0
evens = list(filter(is_even, nums))
doubled = list(map(lambda n: n * 2, nums))
print(evens, doubled)
