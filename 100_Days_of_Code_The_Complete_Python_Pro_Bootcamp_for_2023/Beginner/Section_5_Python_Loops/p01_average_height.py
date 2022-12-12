"""
You are going to write a program that calculates the average student height from a List of heights.
Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality
using what you have learnt about for loops.
"""

student_height = [int(height) for height in input().split()]
total_height = 0
number_of_students = 0
for height in student_height:
    total_height += height
    number_of_students += 1

avr_height = total_height / number_of_students
print(round(avr_height))
