"""
You are going to write a program that calculates the highest score from a List of scores.
Important you are not allowed to use the max or min functions.
"""

student_scores = [int(num) for num in input().split()]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f'The highest score in the class is: {max_score}')
