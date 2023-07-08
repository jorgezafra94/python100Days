print("Welcome to the tip calculator")
bill_amount = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
number_persons = input("How many people to split the bill? ")

bill_amount_fl = float(bill_amount)
percentage_int = int(percentage)
number_persons_int = int(number_persons)

total_amount = (bill_amount_fl + (bill_amount_fl * (percentage_int / 100)))

total_amount_per_person = round(total_amount / number_persons_int, 2)
print(f'Each person should pay: ${total_amount_per_person}')