import random

num = random.randint(1, 101)
guessed_numbers = [0]

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")


while True:
    guess_num = int(input())
    if guess_num < 1 or guess_num > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    if guess_num == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guessed_numbers)} GUESSES!!')
        break

    guessed_numbers.append(guess_num)

    if guessed_numbers[-2]:
        if abs(num - guess_num) < abs(num - guessed_numbers[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num - guess_num) <= 10:
            print('WARM!')
        else:
            print('COLD!')








