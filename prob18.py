# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def even_or_odd(n):
    if n %2 == 0:
        return 'the given num is even'
    else:
        return 'the given num is odd'


print (even_or_odd(3))
print( even_or_odd(2))