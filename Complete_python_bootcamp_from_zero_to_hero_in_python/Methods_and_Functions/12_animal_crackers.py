
def animal_crackers(content):

    words = content.split()
    return words[0][0].lower() == words[1][0].lower()

print(animal_crackers("Crazy Kangaroo"))
