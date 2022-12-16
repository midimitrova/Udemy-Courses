from math import ceil


def prime_checker(number):
    is_prime = True
    for div in range(2, ceil(number / 2) + 1):
        if number % div == 0:
            is_prime = False
            break
    if is_prime:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')


prime_checker(73)
