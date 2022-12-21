import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def difficulty():
    user_input = input("Choose a difficulty. Type 'easy' or 'hard'.: ").lower().strip()
    if user_input == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, turns):
    if guess > answer:
        print('Too High.')
        return turns - 1
    elif guess < answer:
        print('Too Low.')
        return turns - 1
    else:
        print(f'You got it! The answer was {answer}.')


def game():
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    user_answer = random.randint(1, 100)

    turns = difficulty()
    guess = 0
    while guess != user_answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, user_answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != user_answer:
            print("Guess again.")


game()
