def master_yoda(content):
    reverse_words = content.split()
    reverse_words.reverse()
    return " ".join(reverse_words)
print(master_yoda('I\' am \'home'))
print(master_yoda('We\' are \'ready'))

