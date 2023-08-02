# Write a Python program to test whether a passed letter is a vowel or not.

def letter_check(le):
    vowels = ["a","e","i","o","u"]
    for i in vowels :
        if i == le:
            return ('the given letter is vowel')
        else:
            return ('its not a vowel')
        
        
def letter_check2(le):
    vowels1= ["a","e","i","o","u"]
    return le in vowels1

    
print (letter_check2("a"))
print (letter_check2("c"))    
print (letter_check("a"))
print (letter_check("b"))