"""
Range function

range function has three parameters.
range(x, y, z)

x -> its going to be the first digit, and it will be included
y -> its going to be the last digit, and it is not going to be included
z -> its going to be the pace, by default it is 1

range(1, 5) -> will go from 1 to 4
range(1, 5, 2) -> 1, 3 because the step is 2 so it will go every each two
range(10, 0, -1) -> descendant order pace -1 to decrease
"""

# sum all number from 1 to 100
acc = 0

for num in range(1, 101):
    acc += num

print(acc)

print("······································")

# print descendant order
for num in range(10, -1, -1):
    print(num)