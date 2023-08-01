# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
# Return the string unchanged if the given string already begins with "Is".

def text(t):
    if len(t)>=2 and t[:2] == "Is":
        return t
    return "Is"+t

print(text("array"))
print(text("Ismaty"))