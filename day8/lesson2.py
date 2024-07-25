"""
function with more than one parameter

be careful with the order of the parameters, so when you are setting the argument
make your they match the one you want, unless you use the keyword
"""


def greet(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location}")


greet("Jorge", "Bogota")

# this way you can change the order because the function will get the values by the keywords
greet(location="Bogota", name="Jorge")