// ======================================
// ROCK PAPER SCISSORS
// MAIN GAME LOGIC
// ======================================


// ======================================
// 1. GAME CONFIGURATION
// ======================================

const choices = ["rock", "paper", "scissors"];


// ======================================
// 2. HTML ELEMENTS
// ======================================

const matchFormat = document.getElementById("match-format");

const startButton = document.getElementById("start-button");

const choiceButtons = document.querySelectorAll(".choice");

const playerScoreDisplay = document.getElementById("player-score");

const computerScoreDisplay = document.getElementById("computer-score");

const playerChoiceDisplay = document.getElementById("player-choice");

const computerChoiceDisplay = document.getElementById("computer-choice");

const resultMessage = document.getElementById("result-message");

const targetScoreDisplay = document.getElementById("target-score");

const roundsPlayedDisplay = document.getElementById("rounds-played");

const matchesPlayedDisplay = document.getElementById("matches-played");

const matchesWonDisplay = document.getElementById("matches-won");

const matchesLostDisplay = document.getElementById("matches-lost");

const matchHistoryDisplay = document.getElementById("match-history");


// ======================================
// 3. GAME VARIABLES
// ======================================

let playerScore = 0;

let computerScore = 0;

let roundsPlayed = 0;

let targetScore = 3;

let currentFormat = 5;

let gameActive = false;


// ======================================
// 4. STATISTICS
// ======================================

function loadStatistics() {

    const savedStatistics = localStorage.getItem("rpsStatistics");

    if (savedStatistics) {

        try {

            const parsed = JSON.parse(savedStatistics);

            return {
                played: Number(parsed.played) || 0,
                won: Number(parsed.won) || 0,
                lost: Number(parsed.lost) || 0,
                history: Array.isArray(parsed.history)
                    ? parsed.history
                    : []
            };

        } catch (error) {

            console.error("Could not load statistics:", error);

        }

    }

    return {
        played: 0,
        won: 0,
        lost: 0,
        history: []
    };

}


let statistics = loadStatistics();


// ======================================
// 5. SAVE STATISTICS
// ======================================

function saveStatistics() {

    localStorage.setItem(
        "rpsStatistics",
        JSON.stringify(statistics)
    );

}


// ======================================
// 6. UPDATE STATISTICS DISPLAY
// ======================================

function updateStatisticsDisplay() {

    matchesPlayedDisplay.textContent = statistics.played;

    matchesWonDisplay.textContent = statistics.won;

    matchesLostDisplay.textContent = statistics.lost;

}


// ======================================
// 7. COMPUTER CHOICE
// ======================================

function getComputerChoice() {

    const randomIndex = Math.floor(
        Math.random() * choices.length
    );

    return choices[randomIndex];

}


// ======================================
// 8. DETERMINE WINNER
// ======================================

function determineWinner(player, computer) {

    if (player === computer) {

        return "draw";

    }

    if (
        (player === "rock" && computer === "scissors") ||
        (player === "paper" && computer === "rock") ||
        (player === "scissors" && computer === "paper")
    ) {

        return "player";

    }

    return "computer";

}


// ======================================
// 9. UPDATE SCOREBOARD
// ======================================

function updateScoreboard() {

    playerScoreDisplay.textContent = playerScore;

    computerScoreDisplay.textContent = computerScore;

    roundsPlayedDisplay.textContent = roundsPlayed;

}


// ======================================
// 10. START GAME
// ======================================

function startGame() {

    currentFormat = Number(matchFormat.value);

    targetScore = Math.floor(currentFormat / 2) + 1;

    playerScore = 0;

    computerScore = 0;

    roundsPlayed = 0;

    gameActive = true;

    targetScoreDisplay.textContent = targetScore;

    updateScoreboard();

    playerChoiceDisplay.textContent = "Your choice: -";

    computerChoiceDisplay.textContent = "Computer choice: -";

    resultMessage.textContent = "Game started! Make your move.";

    startButton.textContent = "RESTART GAME";

    choiceButtons.forEach(button => {

        button.disabled = false;

    });

}


// ======================================
// 11. PLAY ROUND
// ======================================

function playRound(playerChoice) {

    if (!gameActive) {

        return;

    }

    const computerChoice = getComputerChoice();

    const winner = determineWinner(
        playerChoice,
        computerChoice
    );

    roundsPlayed++;

    playerChoiceDisplay.textContent =
        `Your choice: ${playerChoice.toUpperCase()}`;

    computerChoiceDisplay.textContent =
        `Computer choice: ${computerChoice.toUpperCase()}`;


    if (winner === "player") {

        playerScore++;

        resultMessage.textContent = "YOU WON THIS ROUND!";

    }

    else if (winner === "computer") {

        computerScore++;

        resultMessage.textContent = "COMPUTER WON THIS ROUND!";

    }

    else {

        resultMessage.textContent = "IT'S A DRAW!";

    }


    updateScoreboard();

    checkMatchWinner();

}


// ======================================
// 12. CHECK MATCH WINNER
// ======================================

function checkMatchWinner() {

    if (playerScore >= targetScore) {

        finishMatch("player");

    }

    else if (computerScore >= targetScore) {

        finishMatch("computer");

    }

}


// ======================================
// 13. FINISH MATCH
// ======================================

function finishMatch(winner) {

    gameActive = false;

    choiceButtons.forEach(button => {

        button.disabled = true;

    });


    if (winner === "player") {

        statistics.won++;

        resultMessage.textContent =
            "CONGRATULATIONS! YOU WON THE MATCH!";

    }

    else {

        statistics.lost++;

        resultMessage.textContent =
            "GAME OVER! COMPUTER WON THE MATCH.";

    }


    statistics.played++;

    const match = {

        date: new Date().toLocaleString(),

        format: currentFormat,

        playerScore: playerScore,

        computerScore: computerScore,

        winner: winner

    };


    statistics.history.unshift(match);

    // Keep the latest 10 matches
    statistics.history = statistics.history.slice(0, 10);


    saveStatistics();

    updateStatisticsDisplay();

    displayMatchHistory();

}


// ======================================
// 14. DISPLAY MATCH HISTORY
// ======================================

function displayMatchHistory() {

    matchHistoryDisplay.innerHTML = "";

    if (statistics.history.length === 0) {

        const item = document.createElement("li");

        item.textContent = "No matches played yet.";

        matchHistoryDisplay.appendChild(item);

        return;

    }


    statistics.history.forEach(match => {

        const item = document.createElement("li");

        const result = match.winner === "player"
            ? "YOU WON"
            : "COMPUTER WON";

        item.textContent =
            `${match.date} | Best of ${match.format} | ` +
            `${match.playerScore} - ${match.computerScore} | ${result}`;

        matchHistoryDisplay.appendChild(item);

    });

}


// ======================================
// 15. EVENT LISTENERS
// ======================================

startButton.addEventListener("click", startGame);


choiceButtons.forEach(button => {

    button.addEventListener("click", () => {

        const playerChoice = button.dataset.choice;

        playRound(playerChoice);

    });

});


// ======================================
// 16. INITIALISE APPLICATION
// ======================================

choiceButtons.forEach(button => {

    button.disabled = true;

});

updateStatisticsDisplay();

displayMatchHistory();

targetScoreDisplay.textContent = targetScore;

updateScoreboard();