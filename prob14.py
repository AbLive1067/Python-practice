# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def num_within(n):
    return ((abs(1000-n) <= 100) or (abs(2000-n) <= 100))


print (num_within(1000))
print (num_within(800))
print (num_within(1900))
print(num_within(1700))