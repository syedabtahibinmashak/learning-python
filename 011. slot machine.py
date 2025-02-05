import random
import time

def welcome_msg():
    print("")
    print("**************** Welcome to Python Slot Machine Program ****************")
    print("                     Get 💌|💌|💌 for x10 payback")
    print("                     Get 🍕|🍕|🍕 for x08 payback")
    print("                     Get ⚓|⚓|⚓ for x05 payback")
    print("                     Get 👻|👻|👻 for x03 payback")
    print("                     Get 🎈|🎈|🎈 for x02 payback")
    print("************************************************************************")

def goodbye_msg(balance):
    print("")
    print("********************* Game Over! Thanks for Playing! ********************")
    print(f"                            Your Balance: ${balance}")
    print("*************************************************************************")

def scan_bet(balance):
    while True:
        bet = input("Enter Your Bet : $")
        if not bet.isdigit():
            print("Enter Valid Number!")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient Funds!")
            continue
        elif bet <= 0:
            print("Invalid Bet Amount!")
            continue
        else:
            return bet

def spin_roll():
    symbols = ["🎈", "🍕", "⚓", "💌", "👻"]
    result = [random.choice(symbols) for _ in range(3)]
    print("")
    print("...spinning...spinning...")
    time.sleep(1)
    print(f"Your Roll: {result[0]} | {result[1]} | {result[2]}")

    if result[0] == result[1] == result[2]:
        print("Congratulations! You Win!")
        if result[0] == "💌":
            return 10
        elif result[0] == "🍕":
            return 8
        elif result[0] == "⚓":
            return 5
        elif result[0] == "👻":
            return 3
        elif result[0] == "🎈":
            return 2
    else:
        print("Sorry! You Lose!")
        return 0

def try_again():
    again = input("Want to try again? (y/n): ").lower()
    if again == "y":
        return True
    else:
        return False

def main():
    balance = 100
    welcome_msg()

    while True:
        print("")
        print(f"Current Balance: ${balance}")
        bet = scan_bet(balance)
        balance -= bet
        balance += spin_roll() * bet
        if balance == 0:
            break
        else:
            print("")
            print(f"Current Balance: ${balance}")
        if not try_again():
            break
    goodbye_msg(balance)

if __name__ == "__main__":
    main()
