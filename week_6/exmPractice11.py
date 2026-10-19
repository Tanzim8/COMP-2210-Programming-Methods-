inventory = {
    "Laptop": (800, 5),
    "Mouse": (25, 10),
    "Keyboard": (50, 4)
}

orders = [
    ("Laptop", 2),
    ("Mouse", 3),
    ("Keyboard", 6),
    ("Laptop", 2),
    ("Monitor", 1),
    ("Mouse", 5)
]

total_rev = 0
reject_count = 0
for item,quantity in orders:
    if item in inventory:
        price,stock = inventory[item]
        if(stock < quantity):
            print(item,"Not eough in stock")
            reject_count += 1
        elif stock>=quantity :
            stock -= quantity
            total_rev += price*quantity
            inventory[item] = price,stock
        # print("Available")
    else:
        print(item,"Not available")
        reject_count += 1
print("Total Revenue: ", total_rev)
print("Orders Rejected: ", reject_count)
print("Updated inventory: ", inventory)