"""
This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

The input is going to be like A1, B2, C3. Where A, B, C are the columns and 1, 2, 3 the rows
"""
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
get_col = position[0]
get_row = int(position[1]) - 1
col_positions = ['A', 'B', 'C']
get_col = col_positions.index(get_col)
map[get_row][get_col] = 'X'
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
