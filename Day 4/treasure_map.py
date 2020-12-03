# -*- Encoding: UTF-8 -*-

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))

position_separated = [int(i) for i in str(position)]

position_row = position_separated[0]
position_column = position_separated[1]

map[position_row - 1][position_column - 1] = "X  "

print(f"{row1}\n{row2}\n{row3}")
