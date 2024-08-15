"""
debugging
"""

from random import randint
dice_images = [":)", ":)", ":)", ":)", ":)", ":)"]
dice_num = randint(0, 6)
print(dice_images[dice_num])

# What is the problem? -> when you run the program more than once
# you will find that at some point there is an error
# what is the error? -> it is a list index out of range
# when that happens? -> when dice_num takes the value of 6
# how can you fix it? -> changing th randint to 0 - 5 or adding one more dice_image
