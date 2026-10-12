products = ["Milk", "Bread", "Eggs", "Apples", "Rice"]
prices = (4.50, 3.00, 5.50, 4.00, 8.00)
totalPrice = 0
priceFour = 0
for product,price in zip(products,prices):
    print(product)
    userNeed = int(input("Enter quantity: "))
    print("Price per unit: ",price)
    totalPrice += price*userNeed
    if price > 4.00:
        priceFour+=1
    if price > 5.00:
        print("Expensive")
    else:
        print("Affordable")

priceAvg = sum(prices)/len(prices)

print("Total cart price: ", totalPrice)
print("Product costing more than $4: ", priceFour)
print("Price average: ", priceAvg)


