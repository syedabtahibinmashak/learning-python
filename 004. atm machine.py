print("")
print("*************** Welcome to Python ATM Machine ***************")
print("")
print("1: Check Balance")
print("2: Deposit Money")
print("3: Withdraw Money")
print("4: Exit Program")

balance = 0
while True:
    print("")
    option = input("Input Choice (1-4): ")

    if option == "1":
        print(f"Your Balance: ${balance:.2f}")
        continue

    elif option == "2":

        amount = input("Enter Deposit Amount: $")
        if not amount.isdigit() or float(amount) == 0:
            print("Invalid Amount!")
            continue
        amount = float(amount)
        balance += amount
        print(f"Successfully Deposited ${amount:.2f}")
        continue

    elif option == "3":

        amount = input("Enter Withdraw Amount: $")
        if not amount.isdigit() or float(amount) == 0:
            print("Invalid Amount!")
            continue
        if float(amount) > balance:
            print("Insufficient Balance!")
            continue
        amount = float(amount)
        balance -= amount
        print(f"Successfully Withdrawn ${amount:.2f}")
        continue

    elif option == "4":
        break

    else:
        print("Invalid Choice!")

print("")
print("**************** Thank You! Have a Nice Day! ****************")
