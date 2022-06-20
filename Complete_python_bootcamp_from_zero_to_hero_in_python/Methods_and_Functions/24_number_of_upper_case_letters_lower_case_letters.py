def up_low(mystring):
    d = {'up_cnt':0, 'low_cnt':0}
    for letter in mystring:
        if letter.isupper():
            d['up_cnt'] += 1
        elif letter.islower():
            d['low_cnt'] += 1
        else:
            pass

    print(f'Original String : {mystring}')
    print(f'No. of Upper case characters :  {d["up_cnt"]}')
    print(f'No. of Lower case Characters :  {d["low_cnt"]}')
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


