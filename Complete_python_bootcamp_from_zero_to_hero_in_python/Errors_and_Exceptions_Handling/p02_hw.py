def my_func():
    x = 5
    y = 0
    try:
        z = x / y
        return z
    except:
        print('You can not divide by zero!')
    finally:
        print('All Done.')
my_func()


