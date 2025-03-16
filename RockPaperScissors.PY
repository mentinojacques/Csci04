import random
comp_choices = ['Rock', 'Paper', 'Scissors']
result = ''
play = 'Y'

while(play == 'Y'):
    choice = input('Rock, Paper, Scissors?: \n')
    comp_choice = random.choice(comp_choices)
    if choice == comp_choice:
        result = 'Draw'
    elif choice == 'Rock' and comp_choice == 'Scissors':
        result = 'You Win'
    elif choice == 'Scissors' and comp_choice == 'Paper':
        result = 'You Win'
    elif choice == 'Paper' and comp_choice == 'Rock':
        result = 'You Win'
    else:
        result = "You Lose"

    print("You chose:\n", choice)
    print("Computer chose:\n", comp_choice)
    print(result)
    play = input("Do you want to play again? Y/N \n")
