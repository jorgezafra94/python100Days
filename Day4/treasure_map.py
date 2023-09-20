# basic map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position_col_row = input("Where do you want to put the treasure? ")
position_row_col = [position_col_row[p] for p in range(len(position_col_row) - 1, -1, -1)]
row = int(position_row_col[0]) - 1
col = int(position_row_col[1]) - 1

map[row][col] = 'X'

print(f"{row1}\n{row2}\n{row3}")