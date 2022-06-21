import string

def ispangram(str1, alphabet = string.ascii_lowercase):
    alphabet = set(alphabet)
    str1 = str1.replace(" ", "")
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphabet
print(ispangram("The quick brown fox jumps over the lazy dog"))
