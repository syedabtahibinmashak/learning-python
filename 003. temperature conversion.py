print("")
print("*************** Welcome to Python Temperature Converter ***************")
print("")
print("1. Celsius to Fahrenheit ")
print("2. Celsius to Kelvin ")
print("3. Fahrenheit to Celsius ")
print("4. Fahrenheit to Kelvin ")
print("5. Kelvin to Celsius ")
print("6. Kelvin to Fahrenheit ")
print("")

while True:
    method = input("Select Conversion Method (1-6): ")

    if method == "1":
        c = float(input("Enter Temperature in Celsius Scale: "))
        f = ((c / 5) * 9) + 32
        print(f"Temperature in Fahrenheit Scale: {f:.2f}")
        break

    elif method == "2":
        c = float(input("Enter Temperature in Celsius Scale: "))
        k = c + 273.15
        print(f"Temperature in Kelvin Scale: {k:.2f}")
        break

    elif method == "3":
        f = float(input("Enter Temperature in Fahrenheit Scale: "))
        c = ((f - 32) / 9) * 5
        print(f"Temperature in Celsius Scale: {c:.2f}")
        break

    elif method == "4":
        f = float(input("Enter Temperature in Fahrenheit Scale: "))
        k = ((f - 32) / 9) * 5 + 273.15
        print(f"Temperature in Kelvin Scale: {k:.2f}")
        break

    elif method == "5":
        k = float(input("Enter Temperature in Kelvin Scale: "))
        c = k - 273.15
        print(f"Temperature in Celsius Scale: {c:.2f}")
        break

    elif method == "6":
        k = float(input("Enter Temperature in Kelvin Scale: "))
        f = ((k - 273.15) / 5) * 9 + 32
        print(f"Temperature in Fahrenheit Scale: {f:.2f}")
        break

    else:
        print("Invalid Selection!")

print("")
print("******************* Thanks for Using this Converter *******************")
