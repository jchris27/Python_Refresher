import random
import sys

def guess_my_number(name="Player One"):
    game_count = 0
    player_wins = 0


    def play_guess_my_number():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins

        player_choice = input(f"\nHi {name}! guess which number I'm thinking of... 1, 2, or 3?\n\n")

        computer_choice = random.choice("123")

        if player_choice not in ["1", "2", "3"]:
            print(f"\nSorry {name}, but you can only choose between 1 - 3.")
            print("\n\nLet's try again..\n")
            return guess_my_number(name)

        print(f"\n{name}, you chose {player_choice}.")
        print(f"I was thinking about the number {computer_choice}.\n")

        player = int(player_choice)
        computer = int(computer_choice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            if player == 1 and computer == 1:
                player_wins += 1
                return f"{name}, you win! 🥳\n"
            elif player == 2 and computer == 2:
                player_wins += 1
                return f"{name}, you win! 🥳\n"
            elif player == 3 and computer == 3:
                player_wins += 1
                return f"{name}, you win! 🥳\n"
            else:
                return f"Sorry, {name}. Better luck next time. 😔\n"
        
        game_result = decide_winner(player, computer)

        game_count += 1
        
        print(game_result)

        print(f"Game count: {game_count}\n")
        print(f"{name}'s wins: {player_wins}\n")
        print(f"Your winning percentage: {player_wins/game_count:.2%}%\n")

        print(f"Play again, {name}?")

        while True:
            play_again = input("\nY for Yes or \nQ to Quit\n\n")

            if play_again.lower() not in ["y", "q"]:
                print(f"Sorry {name}, but you can only choose between Y or Q.")
                continue
            else:
                break
        if play_again.lower() == "y":
            return play_guess_my_number()
        else:
            print("\n\n🎉 🎉 🥳 🎉 🎉\n\n")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return
    return play_guess_my_number

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personlaize name for the person playing the game."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()
    guess_number = guess_my_number(args.name)
    guess_number()