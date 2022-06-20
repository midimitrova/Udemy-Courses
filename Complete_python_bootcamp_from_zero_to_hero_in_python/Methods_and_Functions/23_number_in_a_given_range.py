def ran_check(num, low, high):
    if num in range(low, high + 1):
        return (f'{num} is in the range between {low} and {high}')
    else:
        return (f'{num} is not in the range between {low} and {high}')
print(ran_check(5, 2, 7))



# second solution
# def ran_check(num, low, high):
#     if num in range(low, high + 1):
#         return True
#     else:
#         return False
# print(ran_check(5, 2, 7))