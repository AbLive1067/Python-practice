# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def sum_of_three(a,b,c):
    if a==b==c:
        return (a+b+c)*3
    else :
        return (a+b+c)


print (sum_of_three(1,2,3))
print (sum_of_three(3,3,3))
