"""
Instructions:
You are going to write a program that will select a random name from a list of names. The person selected will have to
pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
"""

import random
names = input().split(', ')
random_names = random.randint(0, (len(names) - 1))
print(f'{names[random_names]} is going to buy the meal today!')