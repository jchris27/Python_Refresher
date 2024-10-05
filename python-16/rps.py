import sys
import random
from enum import Enum
import os

def rps(name="Player_One"):
    clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        from arcade import arcade
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("\nLet\'s Play Rock, Paper or Scissors!\n\n")

        player_choice = input(f"{name}, please enter a number...\n 1 for ROCK\n 2 for PAPER\n 3 for SCISSORS:\n\n")

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
            print(f"{name} , please enter 1, 2, or 3 only.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        player_emoji = str(RPS(player)).replace("RPS.", "")
        computer_emoji = str(RPS(computer)).replace("RPS.", "")

        print(f"{name} chose {player_emoji}")
        print(f"Python chose {computer_emoji}\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, you win! 🥳"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}, you win! 🥳"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}, you win! 🥳"
            elif player == computer:
                return "It\'s a DRAW! 😳"
            else:
                python_wins += 1
                return f"🐍 Python wins! Sorry {name}... 🥺"
        
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name} score: {player_wins}")
        print(f"\nPython score: {python_wins}")

        print(f"\n\nWould you like to play again {name}?")

        while True:
            play_again = input("\n\nY for Yes \nQ for Quit \n\n")

            if play_again.lower() not in ["y", "q"]:
                print(f"\n{name}, please choose between Y or Q only.")
                continue
            else:
                if play_again.lower() == "y":
                    clear()
                    play_rps()
                else:
                    print("\n\n🎉 🎉 🥳 🎉 🎉\n\n")
                    print("Thank you for playing!\n")
                    # sys.exit(f"Bye {name}! 👋")
                    # print(f"Bye {name}! 👋")
                    # arcade(name)
                    if __name__ == "__main__":
                        sys.exit(f"Bye {name}! 👋")
                    else:
                        return
    return play_rps




if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalize name for the person playing the game."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()