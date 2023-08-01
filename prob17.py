# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

def copies(s,n):
    all = ""
    for i in range (n):
        all += s
    return all

print (copies("asset",4))