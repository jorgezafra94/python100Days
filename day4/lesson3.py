"""
first steps with lists

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

# to create a list we can do it in these ways
list1 = []
list2 = list()
print(list1, list2)

# if we want to add an element to the list we can use append or insert
list1.append(4)
list1.append(2)

list2.insert(0, 5)
list2.insert(0, 9)

print(list1, list2)

# to create a copy of an existing list we can use copy method
list3 = list1.copy()
print(list3)

# if we want to join two list we can use extend method
list3.extend(list2)
print(list3)

# if you want to clear a list
list3.clear()
print(list3)

# if you want to remove elements by position
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list4)
list4.pop()  # will remove the last element by default
print(list4)
list4.pop(2)  # will remove the element in position 2
print(list4)

# if you want to remove elements by value use remove
# this one will delete the first occurrence
list4.remove(2)

# if we have an element repeated in a list we can get the number of times it is in the list
list4 = [1, 2, 3, 3, 5, 5, 5, 10, 9, 10]
num3 = list4.count(3)
num5 = list4.count(5)
print(num3, num5)

# if you want to know what is the index of an element
# it will bring the index of the first occurrence
my_idx = list4.index(5)
print(my_idx)

# if you want to reverse the list
print(list4)
list4.reverse()
print(list4)
