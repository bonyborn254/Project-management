import random
import time

def aviator_game():
    print("Welcome to the Aviator Game!")
    balance = 100  # Starting balance
    print(f"Your starting balance is ${balance}")

    while balance > 0:
        print("\n--- New Round ---")
        print(f"Your current balance: ${balance}")
        try:
            bet = float(input("Enter your bet amount (or type 0 to quit): "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if bet == 0:
            print(f"You are leaving with ${balance}. Thanks for playing!")
            break
        elif bet > balance or bet <= 0:
            print("Invalid bet! Bet must be within your balance and greater than 0.")
            continue

        print("The round is starting! Watch the multiplier grow...")
        multiplier = 1.0
        crash_point = random.uniform(1.5, 5.0)  # Random crash point between 1.5x and 5.0x

        while True:
            time.sleep(0.5)  # Simulate time passing
            multiplier += 0.1  # Increment multiplier
            print(f"Multiplier: {multiplier:.1f}x", end="\r")

            if multiplier >= crash_point:
                print(f"\nThe multiplier crashed at {crash_point:.1f}x!")
                print("You lost your bet!")
                balance -= bet
                break

            cash_out = input("Type 'cashout' to cash out or press Enter to continue: ").strip().lower()
            if cash_out == "cashout":
                winnings = bet * multiplier
                print(f"You cashed out at {multiplier:.1f}x and won ${winnings:.2f}!")
                balance += winnings - bet
                break

    if balance <= 0:
        print("You ran out of money! Game over.")

if __name__ == "__main__":
    aviator_game()