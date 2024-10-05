import sys
import random
from enum import Enum

game_count = 0

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print("")

    player_choice = input("Let\'s Play Rock, Paper or Scissors!\n\nChoose a number...\n 1 for ROCK\n 2 for PAPER\n 3 for SCISSORS:\n\n")

    print("")
    
    # try:
    #     player = int(player_choice)
    # except ValueError:
    #     print("Invalid value, Please choose between 1 - 3 only.")
    #     sys.exit()

    # if player < 1 or player > 3:
    #     print("Invalid value, Please choose between 1 - 3 only.")
    #     sys.exit()

    if player_choice not in ["1", "2", "3"]:
        print("Invalid value, Please choose between 1 - 3 only.")
        play_rps()

    player = int(player_choice)

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    player_emoji = str(RPS(player)).replace("RPS.", "")
    computer_emoji = str(RPS(computer)).replace("RPS.", "")

    print(f"You chose {player_emoji}")
    print(f"Python chose {computer_emoji}\n")

    def game_stat(player, computer):
        if player == 1 and computer == 3:
            return "You win! 🥳"
        elif player == 2 and computer == 1:
            return "You win! 🥳"
        elif player == 3 and computer == 2:
            return "You win! 🥳"
        elif player == computer:
            return "It\'s a DRAW! 😳"
        else:
            return "Python wins! 🐍"
    
    game_result = game_stat(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: "+ str(game_count))

    print("\n\nPlay again?")

    while True:
        play_again = input("\n\nY for Yes \nQ for Quit \n\n")

        if play_again.lower() not in ["y", "q"]:
            print("\nInvalid value, please choose between Y or Q only.")
            continue
        else:
            if play_again.lower() == "y":
                play_rps()
            else:
                print("\n\n🎉 🎉 🥳 🎉 🎉\n\n")
                print("Thank you for playing!\n")
                sys.exit("Bye! 👋")


play_rps()