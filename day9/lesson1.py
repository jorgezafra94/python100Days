"""
dictionaries

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""

# create empty dictionaries
my_d = {}
my_d1 = dict()

# create dictionaries with elements
# dictionaries can have a mix in their values
my_d2 = {"key1": "value1", "key2": 123}

# adding element to dictionaries
my_d.update({"key1": "value1"})
my_d["key3"] = ['a', 1, 'b']
print(my_d)

# create a copy
dict_copy = my_d.copy()
print(dict_copy)

# clear a dictionary
dict_copy.clear()
print(dict_copy)

# create a dictionary fromkeys
# y is going to be the same for everyone
x = ('a', 'b', 'c')
y = ('1', '2', '3')
fk_dict = dict.fromkeys(x, y)
print(fk_dict)

# get the value of a key
# [] and get bring the value of a key, but one throws an error while the other don't
print(fk_dict.get('a'))
print(fk_dict['a'])
# in case the key does not exist we can throw a default value
print(fk_dict.get('d', "prueba"))

# get a list of tuples with keys and values
print(list(my_d.items()))

# get the keys of a dictionary
print(list(fk_dict.keys()))

# get the values of a dictionary
print(list(fk_dict.values()))

# eliminate the element of the specified key
print(fk_dict)
fk_dict.pop('b')
print(fk_dict)
print()

# using for loop
# a regular for loop will return just the keys
for k in fk_dict:
    print(k)
print()
# this one will bring keys and values but as we use _ we are going to omit the keys
for _, v in fk_dict.items():
    print(v)
print()
for k, v in fk_dict.items():
    print(k, v)
