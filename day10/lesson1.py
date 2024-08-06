"""
functions with return

all we have to do is use "return"
"""


def my_func():
    result = 2 * 3
    return result


def my_func1(x, y):
    join = x + y
    join = join.upper()
    return join


answer = my_func()
print(answer)

answer = my_func1("paper", "joy")
print(answer)