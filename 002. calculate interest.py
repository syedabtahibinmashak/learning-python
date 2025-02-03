print("")
print("**************** Welcome to Python Interest Calculator ****************")
print("")
principal = rate = time = 0

while principal <= 0:
    principal = float(input("Enter Principal Amount: "))
    if principal <= 0:
        print("Invalid Amount!")

while rate <= 0:
    rate = float(input("Enter Rate of Interest: "))
    if rate <= 0:
        print("Invalid Rate of Interest!")

while time <= 0:
    time = float(input("Enter Time in Years: "))
    if time <= 0:
        print("Invalid Time!")

total = principal * (1 + rate / 100) ** time
print("")
print(f"Total Amount after {time} year(s): {total:.02f} ")
print("")
print("******************* Thanks for Using this Calculator ******************")
