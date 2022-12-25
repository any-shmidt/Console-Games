import random


print('Rock Paper Scissors')


def play_again():
    again = input('Play again? yes / no : ').lower()
    while not again.startswith(('y', 'n')):
        again = input('Play again? yes / no : ').lower()
    return again.startswith('y')

            
def game():

    play_game = True

    rock = """
    ____
___'    )
    (____)
    (____)
    (___)
----(__)
"""
    scissors = """
    ____
---' ___)____
       ______)
     _________)
     (___)
---._(__)
"""
    paper = """
    ____
---'    )_____
      ________)
      _________)
     _________)
---._________)
"""

    list1 = [rock, paper, scissors]

    while play_game:
        choice = input('rock - 0, scissors - 1, paper - 2: ')

        if choice == '0':
            choice = rock
        if choice == '1':
            choice = scissors
        if choice == '2':
            choice = paper
    
        print(choice)

        computer_choice = random.choice(list1)
        print(f'Computer:\n{computer_choice}')

        if choice == rock and computer_choice == scissors:
            print('You win')
        if choice == rock and computer_choice == paper:
            print('You lose')
        if choice == scissors and computer_choice == rock:
            print('You lose')
        if choice == scissors and computer_choice == paper:
            print('You win')
        if choice == paper and computer_choice == rock:
            print('You win')
        if choice == paper and computer_choice == scissors:
            print('You lose')
        if choice == computer_choice:
            print('Drawn game')
        play_game = False

game()
while play_again():
    game()