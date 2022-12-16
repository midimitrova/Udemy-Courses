from math import ceil
"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
"""


def paint_calc(height, width, cover):
    num_of_cans = (height * width) / cover
    print(f'You\'ll need {ceil(num_of_cans)} cans of paint.')


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
