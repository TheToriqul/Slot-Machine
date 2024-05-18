# Slot Machine Game

Welcome to the Slot Machine Game! This is a simple slot machine simulation written in Python. Players can deposit money, place bets, and spin the slot machine to win or lose money based on the outcomes.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to Play](#how-to-play)
- [Code Explanation](#code-explanation)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [License](#license)

## Introduction

This slot machine game allows players to:

- Deposit money into their account.
- Choose the number of lines to bet on.
- Place bets on each line.
- Spin the slot machine to win or lose money based on the outcome.

## Features

- Random slot machine spins.
- Multiple betting lines.
- Different symbols with varying values and probabilities.
- Easy-to-use command-line interface.

## How to Play

1. **Deposit Money**: Start by depositing an amount of money.
2. **Select Lines**: Choose the number of lines to bet on (up to 3 lines).
3. **Place Bet**: Place a bet amount for each line.
4. **Spin**: Spin the slot machine and see the outcome.
5. **Repeat or Quit**: Continue spinning as long as you have money, or quit the game to end.

## Code Explanation

### Constants

- `MAX_LINES`: Maximum number of betting lines.
- `MAX_BET`: Maximum bet amount per line.
- `MIN_BET`: Minimum bet amount per line.
- `ROWS` and `COLS`: Dimensions of the slot machine grid.
- `symbol_count`: Dictionary mapping each symbol to its count in the slot machine.
- `symbol_value`: Dictionary mapping each symbol to its value when forming a winning line.

### Functions

- `check_winnings(columns, lines, bet, values)`: Checks for winnings based on the slot machine spin, number of lines bet, and bet amount.
- `get_slot_machine_spin(rows, cols, symbols)`: Generates a random spin for the slot machine.
- `print_slot_machine_spin(columns)`: Prints the slot machine spin result in a formatted way.
- `deposit()`: Prompts the user to deposit money.
- `get_number_of_lines()`: Prompts the user to select the number of lines to bet on.
- `get_bet()`: Prompts the user to place a bet amount per line.
- `game_spin(balance)`: Handles a single spin of the slot machine, including betting and determining the outcome.
- `main()`: The main function that runs the game loop.

### Main Game Loop

The game loop runs in the `main()` function, where the player is prompted to deposit money, place bets, and spin the slot machine until they decide to quit.

## Requirements

- Python 3.x

## How to Run

1. **Clone the repository**:
    ```sh
    git clone https://github.com/TheToriqul/Slot-Machine.git
    cd Slot-Machine
    ```

2. **Run the game**:
    ```sh
    python app.py
    ```

3. Follow the on-screen instructions to play the game.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy the game and good luck! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.