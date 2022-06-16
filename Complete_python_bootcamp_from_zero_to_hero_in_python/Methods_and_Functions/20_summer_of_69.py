def sum_numbers(arr):
    total_sum = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total_sum += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total_sum
print(sum_numbers([1, 3, 5]))
print(sum_numbers([4, 5, 6, 7, 8, 9]))
print(sum_numbers([2, 1, 6, 9, 11]))



