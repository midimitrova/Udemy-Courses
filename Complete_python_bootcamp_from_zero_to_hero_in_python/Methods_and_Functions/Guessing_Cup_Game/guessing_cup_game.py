from random import shuffle

print("WELCOME TO GUESSING CUP GAME!")
print("We have three cups and under one we have one ball --> 'A'.")
print("Pick a number between 1 to 3.")
print("If you guess where is the ball, you win otherwise you lose.")
print("LET'S PLAY!")


my_list = [" ", "A", " "]
def shuffle_my_list(my_list):
    shuffle(my_list)
    return my_list


def player_guess():
    guess = ""
    while guess not in["0", "1", "2"]:
        guess = input("Pick a number: 0, 1 or 2: ")
    return int(guess)


def check_guess(my_list, guess):
    if my_list[guess] == "A":
        print("Correct!")
    else:
        print("Wrong!")
        print(my_list)


mixedup_list = shuffle_my_list(my_list)
guess = player_guess()
check_guess(mixedup_list, guess)


