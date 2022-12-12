"""
You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
"""

even_sum = 0
for num in range(2, 101, 2):
    even_sum += num
print(even_sum)
