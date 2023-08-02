# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
# Return n copies of the whole string if the length is less than 2.

def n_copies(st, n):
    if len(st) <=2:
        line = st * n
        return line
    else :
        line = n* (st[:2])
        return line


print (n_copies("absdewsdf", 3))
print (n_copies("a", 3))