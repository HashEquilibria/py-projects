# basic rock paper scissors game
print("rock beats scissors, scissors beats paper, paper beats rock. Press [Enter] to quit")

import random

AI = ["rock", "paper", "scissors"]

while True:
    print("\nWhat will you choose?")
    player = input()
    pc = random.choice(AI)
    print("you picked", player, "and the computer picked", pc)

    if player == pc:
        print("Tie!")

    elif player == 'rock':
        if pc == 'scissors':
            print("You win!")
        else:
            print("Computer wins!")

    elif player == 'scissors':
        if pc == 'paper':
            print("You win!")
        else:
            print("Computer wins!")

    elif player == 'paper':
        if pc == 'rock':
            print("You win!")
        else:
            print("Computer wins!")

    if player == "":
        print("Game over!")
        break
