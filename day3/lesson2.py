"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
"""

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
under_weight = "you are underweight."
normal_weight = "you have a normal weight."
slightly_over_weight = "you are slightly overweight."
obese = "you are obese."
clinical_obese = "you are clinically obese."

bmi = weight/(height ** 2)
message = f"Your BMI is {bmi}, "

if bmi < 18.5:
    message += under_weight
elif bmi < 25:
    message += normal_weight
elif bmi < 30:
    message += slightly_over_weight
elif bmi < 35:
    message += obese
else:
    message += clinical_obese

print(message)