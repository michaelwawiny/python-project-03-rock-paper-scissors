import random


# Available game choices
CHOICES = ["rock", "paper", "scissors"]


# Generate computer choice
def get_computer_choice():
    return random.choice(CHOICES)


# Get player's choice
def get_player_choice():

    while True:

        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1-3): ").strip()

        options = {
            "1": "rock",
            "2": "paper",
            "3": "scissors"
        }

        if choice in options:
            return options[choice]

        print("Invalid choice! Please select 1, 2 or 3.")


# Determine round winner
def determine_winner(player, computer):

    if player == computer:
        return "draw"

    winning_combinations = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper")
    }

    if (player, computer) in winning_combinations:
        return "player"

    return "computer"


# Play one round
def play_round():

    player = get_player_choice()

    computer = get_computer_choice()

    print("\nYour choice:", player.capitalize())
    print("Computer choice:", computer.capitalize())

    winner = determine_winner(player, computer)

    if winner == "player":
        print("You win this round!")

    elif winner == "computer":
        print("Computer wins this round!")

    else:
        print("It's a draw!")

    return winner


# Play a complete match
def play_match(best_of):

    player_score = 0
    computer_score = 0
    draws = 0

    rounds_needed = (best_of // 2) + 1

    print(f"\nMATCH STARTED: BEST OF {best_of}")
    print(f"First to {rounds_needed} wins takes the match!")

    while (
        player_score < rounds_needed
        and computer_score < rounds_needed
    ):

        print("\n--------------------------")
        print(f"Player: {player_score} | Computer: {computer_score}")
        print(f"Draws: {draws}")
        print("--------------------------")

        winner = play_round()

        if winner == "player":
            player_score += 1

        elif winner == "computer":
            computer_score += 1

        else:
            draws += 1

    print("\n========== MATCH RESULT ==========")

    if player_score > computer_score:
        print("CONGRATULATIONS! YOU WON THE MATCH!")

        match_winner = "player"

    else:
        print("COMPUTER WON THE MATCH!")

        match_winner = "computer"

    print(f"Final score: {player_score} - {computer_score}")
    print(f"Total draws: {draws}")

    return {
        "player_score": player_score,
        "computer_score": computer_score,
        "draws": draws,
        "winner": match_winner,
        "best_of": best_of
    }