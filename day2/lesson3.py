"""
Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
"""

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

weeks_per_year = 52

age_years = int(age)
years_left = 90 - age_years

age_weeks = years_left * weeks_per_year
print(f"You have {age_weeks} weeks left")
