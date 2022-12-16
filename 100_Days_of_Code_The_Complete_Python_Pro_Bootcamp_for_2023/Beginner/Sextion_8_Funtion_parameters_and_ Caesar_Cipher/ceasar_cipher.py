def encrypt(word, num):
    encrypt_message = ''
    for letter in word:
        new_letter = chr(ord(letter) + num)
        if not new_letter.isalpha():
            chars_to_end = 122 - ord(letter)
            last_letters = num - chars_to_end
            new_letter = chr(96 + last_letters)
            encrypt_message += new_letter
        else:
            encrypt_message += new_letter
    return encrypt_message


def decrypt(word, num):
    decrypt_message = ''
    for letter in word:
        new_letter = chr(ord(letter) - num)
        if not new_letter.isalpha():
            chars_to_start = abs(96 - ord(letter))
            last_letters = num - chars_to_start
            new_letter = chr(122 - last_letters)
            decrypt_message += new_letter
        else:
            decrypt_message += new_letter
    return decrypt_message


print('The message should consist only alphabet symbols.')
print('If you want to exit the program, type Ctrl + D.')
try:
    while True:
        user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
        if user_input == 'encode':
            valid_word = True
            user_word = input('Type your message:\n').lower().strip()
            for letter in user_word:
                if not letter.isalpha():
                    valid_word = False
                    break
            if not valid_word:
                print('Invalid input. Please, type new message.')
                continue
            user_shift_num = int(input('Type the shift number:\n'))
            print(f'Here is the encoded message: {encrypt(user_word, user_shift_num)}')
        elif user_input == 'decode':
            user_word = input('Type your message:\n').lower().strip()
            user_shift_num = int(input('Type the shift number:\n'))
            print(f'Here is the decoded message: {decrypt(user_word, user_shift_num)}')

except EOFError as e:
    print(e)
