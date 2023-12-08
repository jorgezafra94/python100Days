import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_tpl = ("rock", rock)
paper_tpl = ("paper", paper)
scissors_tpl = ("scissors", scissors)

options = [rock_tpl, paper_tpl, scissors_tpl]
user_option = input("Enter your choise rock, paper, or scissors: ").lower()

# validation user-option
user_choise = None
for tpl in options:
    if tpl[0] == user_option:
        user_choise = tpl

if user_choise is None:
    print(f"{user_option} is not a valid option in this game")
    exit(0)

# get computer option
computer_random_num = random.randint(0, len(options) - 1)
computer_choise = options[computer_random_num]

# rules
user_won_msg = "USER WON!"
pc_won_msg = "COMPUTER WON!"
result = ""
if computer_choise[0] == user_choise[0]:
    result = "DRAW"
elif computer_choise[0] == "rock":
    if user_choise[0] == "paper":
        result = user_won_msg
    else:
        result = pc_won_msg
elif computer_choise[0] == "paper":
    if user_choise[0] == "scissors":
        result = user_won_msg
    else:
        result = pc_won_msg
else:
    if user_choise[0] == "rock":
        result = user_won_msg
    else:
        result = pc_won_msg

print("------------ GAME -------------------")
print("user choise")
print(user_choise[1])

print("----------------------------")
print("computer choise")
print(computer_choise[1])

print("------------- WINNER ---------------")
print(result)
