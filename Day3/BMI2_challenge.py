height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

height_fl = float(height)
weight_fl = float(weight)

bmi = round(weight_fl / (height_fl ** 2))
message = ''

if bmi < 18.5:
    message = "you are underweight"
elif bmi < 25:
    message = "you have a normal weight."
elif bmi < 30:
    message = "you are slightly overweight."
elif bmi < 35:
    message = "you are obese."
else:
    message = "you are clinically obese."

result = f"Your BMI is {bmi}, {message}"
print(result)