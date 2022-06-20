content = 'nurses run'
def palindrome_word(content):
    phrase = content.replace(" ", "")
    word = phrase[::-1]
    return word == phrase
print(palindrome_word(content))


