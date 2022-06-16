word = "macdonald"

def old_macdonald(word):
    letters = list(word)
    for index in range(len(word)):
        if index == 0:
            letters[index] = letters[index].upper()
        elif index == 3:
            letters[index] = letters[index].upper()
    return "".join(letters)
print(old_macdonald(word))






