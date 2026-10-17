inventory = {
    "Apple": (2.5, 5),
    "Banana": (1.5, 0),
    "Orange": (3.0, 4)
}

orders = ["Apple", "Banana", "Orange", "Apple", "Rice"]

totalRev = 0
for item in orders:
    if item in inventory:
        item_price, item_quantity = inventory[item]
        if item_quantity > 0:
            print(item ,"is in there")
            item_quantity -=1
            # print(item_price)
            totalRev += item_price
            inventory[item] = item_price,item_quantity
        else:
            print("Not there")
    else:
        print("Item not available!")
print("Rev: ", totalRev)
print(inventory)