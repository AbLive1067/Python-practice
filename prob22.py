# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def number_check(n, nums):
    return n in nums

print (number_check (3, [1, 5, 8, 3]))
print (number_check (-1, [1, 5, 8, 3]))