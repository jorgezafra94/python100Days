# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
combined_names = name1 + name2

# constants
__true__ = "true"
__love__ = "love"

true_total = 0
for letter in __true__:
    time_letters = combined_names.count(letter)
    true_total += time_letters

love_total = 0
for letter in __love__:
    time_letters = combined_names.count(letter)
    love_total += time_letters

love_score_str = f"{true_total}{love_total}"
love_score = int(love_score_str)

message = ""
if love_score < 10 or love_score > 90:
    message = f"Your score is {love_score}, you go together like coke and mentos."
elif 40 <= love_score <= 50:
    message = f"Your score is {love_score}, you are alright together."
else:
    message = f"Your score is {love_score}."

print(message)
