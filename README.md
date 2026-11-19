# Rock Paper Scissors 🎮

A command-line Rock Paper Scissors game built with Python.

Challenge the computer in a best-of-3, best-of-5 or best-of-7 match. Track your performance and review your previous matches.

## Features

- Player vs Computer gameplay.
- Random computer selections.
- Best of 3, 5 and 7 match formats.
- Automatic winner detection.
- Live match score tracking.
- Persistent game statistics.
- Match history saved in JSON.
- Input validation.
- Automated unit testing.

## Technologies Used

- Python 3
- Random module
- JSON
- OS module
- Datetime module
- Unittest

## Project Structure

```text
project-03-rock-paper-scissors/
│
├── main.py
├── game.py
├── scoreboard.py
├── README.md
├── requirements.txt
│
├── data/
│   └── statistics.json
│
└── tests/
    └── test_game.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/michaelwawiny/python-project-03-rock-paper-scissors.git
```

Enter the project directory:

```bash
cd python-project-03-rock-paper-scissors
```

Run the application:

```bash
python3 main.py
```

## How to Play

1. Select Play Game.
2. Choose your match format.
3. Select Rock, Paper or Scissors.
4. The computer randomly selects its move.
5. The winner of each round earns a point.
6. The first player to reach the required score wins the match.

### Game Rules

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- Identical choices result in a draw.

## Game Menu

1. Play Game
2. View Statistics
3. View Match History
4. Exit

## Running Tests

Run the automated tests using:

```bash
python3 -m unittest discover -s tests -v
```

## Author

Michael Wawiny

GitHub: https://github.com/michaelwawiny

## License

This project is open-source and available for educational purposes.