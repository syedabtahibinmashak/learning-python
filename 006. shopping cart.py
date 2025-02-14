def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print("")
print("******************************** Shopping Cart Program ********************************")
items = []
prices = []
quantities = []
total = 0
while True:
    print("")
    item = input("Name of the Item (Q to Quit): ")
    if item.lower() == "q":
        break
    else:
        items.append(item.capitalize())

        price = input(f"Price of each {item}: $")
        while (not isfloat(price)) or float(price) <= 0:
            print("Invalid Price!")
            price = input(f"Price of each {item}: $")
        prices.append(float(price))

        quantity = input(f"How many {item}(s): ")
        while (not quantity.isdigit()) or int(quantity) == 0:
            print("Invalid Quantity!")
            quantity = input(f"How many {item}(s): ")
        quantities.append(int(quantity))
length = len(items)
print("")
print("======================= YOUR CART =======================")
print("Item           Unit Price       Quantity      Total Price")
for i in range(length):
    print(f"{items[i]:15}${prices[i]:<16.02f}{quantities[i]:<14}${prices[i]*quantities[i]:.02f}")
    total += prices[i]*quantities[i]
print(f"================================ GRAND TOTAL: ${total:.02f}")
print("")
print("**************************** Thanks for Using this Program ****************************")
