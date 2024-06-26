import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Amount must be a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter a number of lines to bet on (1-" + str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and " + str(MAX_LINES) + ".")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet


def game_spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bets = bet * lines
        if total_bets > balance:
            print(f"You do not have enough money to bet ${total_bets}. Your current balance is ${balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bets}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bets 

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        spin = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        balance += game_spin(balance)
    print(f"Your final balance is ${balance}.")


main()