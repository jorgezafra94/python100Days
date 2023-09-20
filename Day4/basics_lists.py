# creating a list
a = []

# lists in python always start with [ and it finishes with ]
b = ["hola", "chao"]

# we can access a value in the list by its position, remember the first position is 0
print(b[1])
print(b[0])
print(b)

# to get the max number of elements in a list, we have to use len() function
# remember that it works the same as the strings
print(len("hola"))
print(len(b))

# In Python we can access to the last item in the list using negative index
# As the same as positive index, we cannot have an index bigger than the length of the list
# otherwise we are going to have an error
print(b[-1])

# to overwrite an element in the list we can do this
b[1] = "New item"
print(b)

# To add an element in at the end of the list we should use append
b.append("appended element")
print(b)

