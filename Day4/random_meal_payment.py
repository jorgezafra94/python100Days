import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

max_number_position = len(names) - 1
random_position = random.randint(0, max_number_position)
winner_name = names[random_position]


print(f"{winner_name} is going to buy the meal today!")

# We also can do this implementing the choise method of random package
winner_name_two = random.choice(names)
print(f"The new person to pay the meal is {winner_name_two}")

