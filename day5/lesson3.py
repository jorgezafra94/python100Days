"""
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
"""

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest = student_scores[0]
for score in student_scores[1:]:
    if score > highest:
        highest = score

print(f"The highest score in the class is: {highest}")
