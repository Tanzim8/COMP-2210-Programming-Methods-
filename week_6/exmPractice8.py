inventory = {
    "Milk": (4.50, 10),
    "Bread": (3.00, 8),
    "Eggs": (5.00, 6)
}


orders = [
    ("Milk", 3),
    ("Bread", 10),
    ("Eggs", 2),
    ("Milk", 4),
    ("Orange", 5)
]
rev = 0

for item,quantity in orders:
    # print(item,quantity)
    if item in inventory:
        itemPrice, itemQty = inventory[item]
        if itemQty >0 and itemQty >= quantity:
            # print(item, "Availabe")
            rev += itemPrice*quantity
            itemQty -= quantity
            inventory[item] = itemPrice, itemQty
        else: 
            print(item, "Not available")
print("Total Revenue: ", rev)
    