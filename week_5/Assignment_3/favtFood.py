favtFood = ["Salmon Teriyaki", "Beef Noodle", "Dragon Chicken", "Alfredo Fettuchini", "Cajun Salmon"]

for food in favtFood:
    print(food)

userFood = input("Enter another food: ")
favtFood.append(userFood)

if "pizza" in [food.lower() for food in favtFood]:
    print("Pizza is in the list!")
else:
    print("Pizza is not in the list!")


