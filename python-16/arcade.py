from rps import rps
from guess_number import guess_my_number
import sys

def arcade(name="Player One"):
    welcome_back = False

    # if welcome_back == True:
    #     print(f"\n{name}, welcome back to the Arcade! 🤖\n")
    # print(f"\n{name}, welcome to the Arcade! 🤖\n")

    # player_choice = input("Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the Arcade.\n\n")

    # if player_choice == "1":
    #     rps(name)
    # elif player_choice == "2":
    #     guess_my_number(name)
    # elif player_choice.lower() == "x":
    #     print("\n\n🎉 🎉 🥳 🎉 🎉\n\n")
    #     print("Thank you for playing!\n")
    #     sys.exit(f"Bye {name}! 👋")
    # else:
    #     arcade(name)
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade! 🤖\n")
        else:
            print(f"\n{name}, welcome to the Arcade! 🤖\n")



        player_choice = input("Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the Arcade.\n\n")

        if player_choice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return arcade(name)
        
        welcome_back = True

        if player_choice == "1":
            play_rps = rps(name)
            play_rps()
        elif player_choice == "2":
            play_guess_number = guess_my_number(name)
            play_guess_number()
        else:
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")


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
    arcade(args.name)

# Choose a game between RPS or GMY game
# press x to exit the arcade
# go back to starting menu to choose which game