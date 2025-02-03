print("")
print("******************* Welcome to Python Calculator *******************")
print("")
print("A: Addition")
print("S: Subtraction")
print("M: Multiplication")
print("D: Division")
print("")

while True:
    operation = input("Enter Operation (A,S,M,D): ").upper()

    if operation == "A":
        x = float(input("Enter First Number : "))
        y = float(input("Enter Second Number: "))
        print(f"Your Answer is     : {x+y:.2f}")
        break

    elif operation == "S":
        x = float(input("Enter Minuend Number   : "))
        y = float(input("Enter Subtrahend Number: "))
        print(f"Your Answer is         : {x-y:.2f}")
        break

    elif operation == "M":
        x = float(input("Enter Multiplicand Number: "))
        y = float(input("Enter Multiplier Number  : "))
        print(f"Your Answer is           : {x*y:.2f}")
        break

    elif operation == "D":
        x = float(input("Enter Dividend Number: "))
        y = float(input("Enter divisor Number : "))
        if y == 0:
            print("Invalid Operation!")
        else:
            print(f"Your Answer is       : {x/y:.2f}")
        break

    else:
        print("Invalid Operation!")

print("")
print("***************** Thanks for Using this Calculator *****************")
