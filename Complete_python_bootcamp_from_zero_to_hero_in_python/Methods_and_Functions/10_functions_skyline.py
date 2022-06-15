word = "anthropomorphism"
def myfunc(word):
    new_string = []
    for index in range(len(word)):
        if index % 2 != 0:
            new_string.append(word[index].upper())
        else:
            new_string.append(word[index].lower())
    return "".join(new_string)
print(myfunc(word))




