import random

points_user = 0
points_computer = 0

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
while True:

    user_input = int(input('Please, choose one of: Type 0 for rock, 1 for paper or 2 for scissors: '))
    if user_input not in [0, 1, 2]:
        print('Invalid input! Please, enter one of: 0 for rock, 1 for paper or 2 for scissors:  ')
        continue
    print(game_images[user_input])

    computer_option = random.randint(0, 2)
    print('Computer choose:')
    print(game_images[computer_option])

    if (user_input == 0 and computer_option == 2) or\
        (user_input == 1 and computer_option == 0) or\
        (user_input == 2 and computer_option == 1):
        points_user += 1
        print('You win!')
    elif user_input == computer_option:
        print('Draw!')
    else:
        points_computer += 1
        print('You lose!')

    if points_user == 5 or points_computer == 5:
        if points_user == 5:
            print('You win the game!')
            break
        else:
            print('You lost the game!')
            break
