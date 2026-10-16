shop = {
    "Price" : "",
    "Stock_Quantity":""
}

userItem = input("Enter the item: ")
userQuantity = int(input("Enter the quantity: "))
shop.update({"Stock_Quantity" : userItem})