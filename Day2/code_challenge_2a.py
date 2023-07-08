# Calculate the BMI body mass index

weight = input("Enter your weight in kg:  ")
height = input("Enter your height in m:  ")

weight_fl = float(weight)
height_fl = float(height)

bmi = int(weight_fl / (height_fl ** 2))

print(bmi)
