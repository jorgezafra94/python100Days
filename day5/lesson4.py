"""
You are going to write a program that calculates the sum of all the even numbers from 1 to X.
If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output.
It should just print the final total and not every step of the calculation.
"""
target = int(input())  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
for i in range(1, target + 1):
    if i % 2 == 0:
        total += i

print(total)
