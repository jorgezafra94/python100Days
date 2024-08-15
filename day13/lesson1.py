"""
Debugging first steps
"""


def my_f():
    for i in range(1, 20):
        if i == 20:
            print("We did it")


my_f()

# Describe the problem
# 1. what is the for loop doing? -> its going through 1 to 19
# 2. when is the function going to print "we did it" -> never cuz i will never get the value of 20
# 3. how would you fix it? -> change the range of i from 1 - 21 of change the condition to 19
