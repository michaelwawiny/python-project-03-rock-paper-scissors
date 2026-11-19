from game import play_match
from scoreboard import display_statistics, display_history, add_match


# Display welcome message
def display_welcome():

    print("\n" + "=" * 40)
    print("       ROCK PAPER SCISSORS")
    print("=" * 40)
    print("Welcome to the ultimate challenge!")
    print("Challenge the computer and win!")
    print("=" * 40)


# Display game menu
def display_menu():

    print("\n========== MAIN MENU ==========")
    print("1. Play Game")
    print("2. View Statistics")
    print("3. View Match History")
    print("4. Exit")
    print("===============================")


# Select match difficulty
def select_match_format():

    formats = {
        "1": 3,
        "2": 5,
        "3": 7
    }

    while True:

        print("\nSelect Match Format:")
        print("1. Best of 3")
        print("2. Best of 5")
        print("3. Best of 7")

        choice = input("Choose (1-3): ").strip()

        if choice in formats:
            return formats[choice]

        print("Invalid selection. Try again.")


# Start a new game
def start_game():

    best_of = select_match_format()

    result = play_match(best_of)

    add_match(result)

    print("\nMatch successfully saved!")


# Main application
def main():

    display_welcome()

    while True:

        display_menu()

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":

            start_game()

        elif choice == "2":

            display_statistics()

        elif choice == "3":

            display_history()

        elif choice == "4":

            print("\nThank you for playing!")
            print("See you next time!")
            break

        else:

            print("\nInvalid option. Please choose 1-4.")


# Run application
if __name__ == "__main__":
    main()