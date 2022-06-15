
def myfunc(*args):
    even_list = []
    for number in args:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass
    return even_list
print(myfunc(1, 2, 3, 4))
