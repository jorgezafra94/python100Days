"""
functions with parameters

parameter is the name of the variable in the function
whereas argument is the value that the parameter is going to take when we call the function
"""


# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greed():
    print("Hello Jorge")
    print("How do you do felipe")
    print("Isn't the weather really nice?")


greed()


# function with input parameter
def greed_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greed_with_name("antonio")
