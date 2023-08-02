# Write a Python program to count the number 4 in a given list.

def num_count_4(numbers):
    count = 0
    for n in numbers:
        if n==4:
            count += 1
    return count


print(num_count_4([1,2,1,4,6,4]))