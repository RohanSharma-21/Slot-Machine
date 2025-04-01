import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a valid amount greater than 0.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines (1 - {MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print("Enter a valid number of lines.")

def get_bet():
    while True:
        amount = input(f"What would you like to bet? (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")

def main():
    balance = deposit()
    total_winnings = 0
    total_loss = 0
    
    while True:
        print(f"Current balance: ${balance}")
        if balance <= 0:
            print("You have no more balance. Game over.")
            break
        
        play = input("Press Enter to play or type 'exit' to quit: ").lower()
        if play == "exit":
            break
        
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough balance. Your current balance is ${balance}.")
            continue
        
        balance -= total_bet
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        
        winnings = random.randint(0, total_bet * 2)
        balance += winnings
        total_winnings += winnings
        total_loss += total_bet
        
        print(f"You won ${winnings}!")
    
    print(f"Total Winnings: ${total_winnings}")
    print(f"Total Loss: ${total_loss}")
    print(f"Final Balance: ${balance}")

if __name__ == "__main__":
    main()
