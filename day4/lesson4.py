"""
You are going to write a program that will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.
"""
import random
people = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
rand_position = random.randint(0, len(people) - 1)
rand_name = people[rand_position]
print(f"{rand_name} is going to buy the meal today!")
