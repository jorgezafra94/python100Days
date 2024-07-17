"""
use random module

the two most used functions are
* randint where you give two limits and it returns an int between these limits
* random where it return a number from 0 - 1 but 1 excluded
"""

import random

num = random.randint(1, 5)
print(num)

num2 = random.random()
print(num2)