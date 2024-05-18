# How to Play the Slot Machine Game

Welcome to the Slot Machine Game! This guide will walk you through the steps to start playing, place bets, and enjoy the game. Follow these simple instructions to get the most out of your gaming experience.

## Step-by-Step Instructions

### 1. Clone the Repository
First, you need to clone the repository from GitHub to your local machine. Open your terminal and run the following commands:

```sh
git clone https://github.com/TheToriqul/Slot-Machine.git
cd Slot-Machine
```

### 2. Run the Game
To start the game, run the `app.py` file using Python:

```sh
python app.py
```

### 3. Deposit Money
The game will prompt you to deposit money into your account. Enter a positive amount to proceed. This will be your starting balance for placing bets.

```plaintext
What would you like to deposit? $
```

### 4. Select the Number of Lines
Next, choose the number of lines you want to bet on. You can bet on up to 3 lines. Enter a number between 1 and 3.

```plaintext
Enter a number of lines to bet on (1-3)?: 
```

### 5. Place Your Bet
Enter the amount you wish to bet on each line. The bet amount must be between $10 and $100.

```plaintext
How much would you like to bet on each line? $
```

### 6. Spin the Slot Machine
After placing your bet, the slot machine will spin, and the result will be displayed. The game will show the outcome of the spin and any winnings.

### 7. Check Your Balance
Your balance will be updated based on the outcome of the spin. The game will display your current balance and prompt you to spin again or quit.

```plaintext
Current balance is $<balance>.
Press enter to play (q to quit).
```

### 8. Repeat or Quit
You can continue playing by pressing Enter or quit the game by typing `q` and pressing Enter. If you decide to continue, repeat steps 4 to 7.

### 9. Game Over
When you quit the game, your final balance will be displayed.

```plaintext
Your final balance is $<balance>.
```

## Tips for Playing

- **Manage Your Bets**: Adjust your bet amount and the number of lines based on your current balance to prolong your gameplay.
- **Understand Symbol Values**: Higher value symbols are less frequent. Aim for combinations of high-value symbols to maximize your winnings.
- **Quit While Ahead**: If you're on a winning streak, consider quitting while you're ahead to secure your winnings.

## Example Gameplay

1. **Deposit Money**:
    ```plaintext
    What would you like to deposit? $100
    ```

2. **Select Lines**:
    ```plaintext
    Enter a number of lines to bet on (1-3)?: 3
    ```

3. **Place Bet**:
    ```plaintext
    How much would you like to bet on each line? $20
    ```

4. **Spin Result**:
    ```plaintext
    You are betting $20 on 3 lines. Your total bet is equal to: $60.
    A | B | C
    D | A | B
    C | C | D
    You won $0.
    You won on lines:
    ```

5. **Next Action**:
    ```plaintext
    Current balance is $40.
    Press enter to play (q to quit).
    ```

---

Enjoy the game and good luck! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/TheToriqul/Slot-Machine).