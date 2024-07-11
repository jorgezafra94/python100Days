"""
Write a program that works out whether if a given year is a leap year.
A normal year has 365 days, leap years have 366, with an extra day in February.
The reason why we have leap years is really fascinating, this video does it more justice.

This is how you work out whether if a particular year is a leap year.

on every year that is divisible by 4 with no remainder

except every year that is evenly divisible by 100 with no remainder

unless the year is also divisible by 400 with no remainder
"""

# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

if year % 4 != 0:
    print("Not leap year")
else:
    if year % 100 != 0:
        print("Leap year")
    else:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
