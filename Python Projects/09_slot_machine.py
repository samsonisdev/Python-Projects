import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {"A": 2,
                "B": 3,
                "C": 4,
                "D": 5}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a amount more than 0.")
        else:
            print("Enter a valid number")

    return amount

def get_no_of_lines():
    while True:
        lines = input("How many lines would like to bet on? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 - {MAX_LINES}")
        else:
            print("Please enter a number")

    return lines

def bet():
    while True:
        bet_amount = input("How much would you like to bet on each line? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Please enter the amount within ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid number")

    return bet_amount

def main():
    balance = deposit()
    lines = get_no_of_lines()
    while True:
        bet_each = bet()
        total_bet = bet_each * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet ${bet_each} on each line. Current Balance: ${balance}")
        else:
            break

    print(f"Doable! You bet ${total_bet}. And your balance is ${balance}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()