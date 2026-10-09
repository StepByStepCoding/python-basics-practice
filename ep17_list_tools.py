# Episode 17: List methods and slicing
# Step By Step Coding · Python basics
#
# Try it: Add nums.append(7) and nums.sort(), then press Run
# Then: Print the first two items with nums[:2], then press Run
# ---------------------------------------------

nums = [5, 3, 8, 1]
nums.append(9)
nums.sort()
print(nums)
nums.remove(8)
print(nums[1:3])
print(nums[-1])
print(nums[::-1])
print(sum(nums), max(nums))
