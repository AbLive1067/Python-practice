# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

name= input("enter the filename:- ")

filename = name.split(".")
print("The extension of the file is :", filename[-1])