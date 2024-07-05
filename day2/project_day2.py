"""
Create Tip calculator
"""

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?: "))
num_people = int(input("How many people to split the bill?: "))

total_to_pay = total_bill + (total_bill * tip / 100)
amount_per_person = round(total_to_pay / num_people, 2)
print(f"Each person should pay: {amount_per_person}")

