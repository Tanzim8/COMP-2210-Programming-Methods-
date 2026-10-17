shop = {
    "Apple":(3, 30),
    "Banana":(2.5, 50),
    "Eggs": (5.5, 16),
    "Milk":(6, 15),
    "Potato":(2, 100),
    "Rice": (2, 200),
    "Mango":(5, 0)
}

totalRevenue = 0

print("shop inventory: ", shop)

print(shop["Apple"])
customerOrder = ["Apple", "Banana", "Rice", "Milk", "Potato", "Apple", "Mango", "Orange"]
for item in customerOrder:
    # print(item)
    if item in shop:
        productPrice, productQty = shop[item]

        if productQty>0:
            print(item, "is available!")
            print(productQty)
            productQty -= 1
            totalRevenue += productPrice
            #Updating the quantity
            shop[item] = productPrice,productQty
        else:
            print(item, "is out of stock!")
    else:
        print(item, "is not available!")
print("Total Revenue: ", totalRevenue)
    
