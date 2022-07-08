def my_func():
    for i in ['a','b','c']:
        try:
            print(i ** 2)
        except:
            print('You can not multiply strings!')
            break

my_func()