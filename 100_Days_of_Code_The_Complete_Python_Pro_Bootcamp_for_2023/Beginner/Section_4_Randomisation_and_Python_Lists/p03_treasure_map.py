"""
Instructions:
You are going to write a program that will mark a spot with an X.
Your job is to write a program that allows you to mark a square on the map using a two-digit system.
The first digit in the input will specify the column (the position on the horizontal axis).
The second digit in the input will specify the row number (the position on the vertical axis).
"""
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
