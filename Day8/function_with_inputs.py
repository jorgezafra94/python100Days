# Argument is the value, and parameter is the name of the variable
# something = 123 -> argument = 123, parameter -> something

# simple function
def greet():
    print("Hello")
    print("How is it going?")
    print("Everything all right?")


# function with parameters
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How is it going {name}?")
    print(f"Everything all right {name}?")


# function with two parameters
def greet_with_name_and_location(name, location):
    print(f"Hello {name}")
    print(f"How is living in {location}?")


# calling functions
greet()
greet_with_name("Jorge")
greet_with_name_and_location("jorge", "Chicago")

# Be careful with positional arguments
greet_with_name_and_location("Chicago", "jorge")
# calling function with keywords
# with this approach the order doesn't matter anymore
greet_with_name_and_location(location="Chicago", name="Jorge")
