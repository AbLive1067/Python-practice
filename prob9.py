# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

import calendar

ye= int(input("enter the value of Year:- "))
mo= int(input("enter the value of Month:- "))
print(calendar.month(ye,mo))
