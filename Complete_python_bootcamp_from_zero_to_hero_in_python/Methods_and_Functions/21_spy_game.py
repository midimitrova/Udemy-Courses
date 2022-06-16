def spy_game(nums):
    mylist = [0, 0, 7, "x"]
    for num in nums:
        if num == mylist[0]:
            mylist.pop(0)

    return len(mylist) == 1
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))