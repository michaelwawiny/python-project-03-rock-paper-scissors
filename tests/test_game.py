import unittest
from unittest.mock import patch

from game import (
    get_computer_choice,
    determine_winner,
    get_player_choice,
    play_match
)


class TestRockPaperScissors(unittest.TestCase):

    # Test computer choice
    def test_computer_choice(self):

        choice = get_computer_choice()

        self.assertIn(
            choice,
            ["rock", "paper", "scissors"]
        )

    # Test draw
    def test_draw(self):

        self.assertEqual(
            determine_winner("rock", "rock"),
            "draw"
        )

    # Test player wins
    def test_player_wins(self):

        self.assertEqual(
            determine_winner("rock", "scissors"),
            "player"
        )

        self.assertEqual(
            determine_winner("paper", "rock"),
            "player"
        )

        self.assertEqual(
            determine_winner("scissors", "paper"),
            "player"
        )

    # Test computer wins
    def test_computer_wins(self):

        self.assertEqual(
            determine_winner("scissors", "rock"),
            "computer"
        )

    # Test player input validation
    @patch("builtins.input", side_effect=["9", "1"])
    def test_player_choice_validation(self, mock_input):

        choice = get_player_choice()

        self.assertEqual(choice, "rock")

    # Test complete match
    @patch("game.play_round", side_effect=["player", "player"])
    def test_player_wins_match(self, mock_round):

        result = play_match(3)

        self.assertEqual(result["winner"], "player")
        self.assertEqual(result["player_score"], 2)
        self.assertEqual(result["computer_score"], 0)


# Run tests
if __name__ == "__main__":
    unittest.main()
