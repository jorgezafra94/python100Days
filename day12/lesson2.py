"""
change a global variable

the second way will show the use of 'global' python keyword
this one will allow us to change a variable outside the scope of
the function
"""

enemies = 1


# first way to change it
def increase_enemies(enemies):
    enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemies


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


# second way to change it
def increase_enemies_2():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies_2()
print(f"enemies outside function: {enemies}")
