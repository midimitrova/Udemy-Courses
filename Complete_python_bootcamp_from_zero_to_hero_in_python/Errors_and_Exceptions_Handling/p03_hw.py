def my_func():
    while True:
        try:
            num = int(input('Please enter a number: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            result = num ** 2
            print(f'Thank you, your number squared is: {result}')
            break
my_func()

