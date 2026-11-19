import json
import os
from datetime import datetime


# Location of the statistics file
DATA_FILE = os.path.join("data", "statistics.json")


# Load saved statistics
def load_statistics():

    if not os.path.exists(DATA_FILE):
        return {
            "matches_played": 0,
            "player_wins": 0,
            "computer_wins": 0,
            "total_draws": 0,
            "history": []
        }

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return {
            "matches_played": 0,
            "player_wins": 0,
            "computer_wins": 0,
            "total_draws": 0,
            "history": []
        }


# Save statistics
def save_statistics(statistics):

    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(statistics, file, indent=4)


# Add a completed match
def add_match(result):

    statistics = load_statistics()

    statistics["matches_played"] += 1

    if result["winner"] == "player":
        statistics["player_wins"] += 1

    else:
        statistics["computer_wins"] += 1

    statistics["total_draws"] += result["draws"]

    match_record = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "best_of": result["best_of"],
        "player_score": result["player_score"],
        "computer_score": result["computer_score"],
        "draws": result["draws"],
        "winner": result["winner"]
    }

    statistics["history"].append(match_record)

    save_statistics(statistics)


# Display statistics
def display_statistics():

    statistics = load_statistics()

    print("\n========== GAME STATISTICS ==========")

    print("Matches played:", statistics["matches_played"])

    print("Your wins:", statistics["player_wins"])

    print("Computer wins:", statistics["computer_wins"])

    print("Total draws:", statistics["total_draws"])

    print("=====================================")


# Display match history
def display_history():

    statistics = load_statistics()

    history = statistics["history"]

    print("\n========== MATCH HISTORY ==========")

    if not history:
        print("No matches played yet.")
        return

    for index, match in enumerate(history, start=1):

        print(f"\nMatch {index}")

        print("Date:", match["date"])

        print("Format: Best of", match["best_of"])

        print(
            "Score:",
            match["player_score"],
            "-",
            match["computer_score"]
        )

        print("Draws:", match["draws"])

        print("Winner:", match["winner"].capitalize())