import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win! 🥳"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win! 🥳"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win! 🥳"
            elif player == computer:
                return "It\'s a DRAW! 😳"
            else:
                python_wins += 1
                return "Python wins! 🐍"
        
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer score: {str(player_wins)}")
        print(f"\nPython score: {str(python_wins)}")

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
    return play_rps


play = rps()
play()