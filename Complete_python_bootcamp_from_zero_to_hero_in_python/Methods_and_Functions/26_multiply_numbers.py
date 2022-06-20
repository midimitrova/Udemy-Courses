my_nums = [1, 2, 3, -4]

def multiply(my_nums):
    total = 1
    for x in my_nums:
        total *= x
    return total
print(multiply(my_nums))