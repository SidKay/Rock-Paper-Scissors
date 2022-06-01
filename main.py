# A simple app that runs the game of rock, paper, scissors.
# Made by Obinna Anya.

import random

def game():
    # This is the list of available selections
    choices = ['R', 'P', 'S']
    # This was created to let the computer specify its choice
    choice_meaning = {
        'R': 'Rock',
        'P': 'Paper',
        'S': 'Scissors'
    }
    player_choice = ''
    computer_choice = ''

    # This loop runs as long as the two players' choices are the same
    # In other words, it will also run again when there is a draw
    while player_choice not in choices:
        player_choice = input("Make a choice. 'R' for rock, 'P' for paper, and 'S' for scissors: ").upper()
        # If the input is not in the list of choices, the code for the if statement
        # runs and asks the user to try again.
        if player_choice not in choices:
            print("Invalid Choice. Try Again.")
        
    # The computer makes a choice
    computer_choice = random.choice(choices)
    print(f"Player ({choice_meaning[player_choice]}) : CPU ({choice_meaning[computer_choice]})")

    # This runs the function containing the game's rules
    game_rules(player_choice, computer_choice)

def game_rules(x, y):
    # x = player's choice, y = computer's choice
    # r > s, s > p, p > r

    # These are the win conditions
    if (x == 'R' and y == 'S') or (x == 'S' and y == 'P') or (x == 'P' and y == 'R'):
        return print("You won! GG")
        
    # The game function gets called again when it's a draw
    elif(x == y):
        print("It's a draw!")
        game()
        return

    # This runs when none of the other conditions are met. In other words, this runs when the computer has won.
    return print("You lost!")

game()