from random import randint, random
import module_example

print(module_example.pi)

# both limits in randint function are included
random_number = randint(1, 999)
print(random_number)

random_float = random() * randint(1, 5)
print(random_float)
