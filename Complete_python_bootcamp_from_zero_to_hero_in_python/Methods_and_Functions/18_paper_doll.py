def paper_doll(content):
    letter = list(content)
    new_string = []
    for i in range(len(letter)):
        letters = letter[i] * 3
        new_string.append(letters)

    return "".join(new_string)
print(paper_doll('Mississippi'))
print(paper_doll('Hello'))