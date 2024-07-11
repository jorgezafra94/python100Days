"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
"""

print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = (name1 + name2).upper()
true_score = 0
love_score = 0

for letter in "TRUE":
    if letter in combined_name:
        true_score += combined_name.count(letter)


for letter in "LOVE":
    if letter in combined_name:
        love_score += combined_name.count(letter)

combined_score = int(f'{true_score}{love_score}')

if combined_score < 10 or combined_score > 90:
    print(f"Your score is {combined_score}, you go together like coke and mentos.")
elif 40 <= combined_score <= 50:
    print(f"Your score is {combined_score}, you are alright together.")
else:
    print(f"Your score is {combined_score}.")
