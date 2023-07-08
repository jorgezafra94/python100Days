x = "Hello"

# we can access some characters of a String using slicing
print(x[0])
print(x[1])

# this one return the last character
print(x[-1])

# We can also convert a string number to an Integer or float
my_str_num = "1234.98764"
new_flt = float(my_str_num)
print(my_str_num, type(my_str_num), new_flt, type(new_flt))

my_str_num = "1234"
new_int = int(my_str_num)
print(my_str_num, type(my_str_num), new_int, type(new_int))