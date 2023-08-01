# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

dt1=date(2014, 7, 2)
dt2=date(2014, 7, 11)

print("The number of days between two dates is", (dt2-dt1).days)