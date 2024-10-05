import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True

while play_again:

# get value from ENUM
# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)

    print("")

    player_choice = input("Let\'s Play Rock, Paper or Scissors!\n\nChoose a number...\n 1 for ROCK\n 2 for PAPER\n 3 for SCISSORS:\n\n")

    print("")
    
    try:
        player = int(player_choice)
    except ValueError:
        print("Invalid value, Please choose between 1 - 3 only.")
        sys.exit()

    if player < 1 or player > 3:
        print("Invalid value, Please choose between 1 - 3 only.")
        sys.exit()

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    player_emoji = str(RPS(player)).replace("RPS.", "")
    computer_emoji = str(RPS(computer)).replace("RPS.", "")

    print(f"You chose {player_emoji}")
    print(f"Python chose {computer_emoji}\n")

    if player == 1 and computer == 3:
        print("You win! 🥳")
    elif player == 2 and computer == 1:
        print("You win! 🥳")
    elif player == 3 and computer == 2:
        print("You win! 🥳")
    elif player == computer:
        print("It\'s a DRAW! 😳")
    else:
        print("Python wins! 🐍")

    play_again = input("\n\nPlay again?\n\nY for Yes or \nQ for Quit \n\n")

    if play_again.lower() == "y":
        continue
    elif play_again.lower() == "q":
        print("\n\n🎉 🎉 🥳 🎉 🎉\n\n")
        print("Thank you for playing!\n")
        play_again = False
    else:
        print("\nInvalid value, please choose between Y or Q only.")
        sys.exit()
sys.exit("Bye! 👋")