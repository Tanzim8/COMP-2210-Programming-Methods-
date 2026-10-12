temperatures = (18, 22, 25, 19, 30, 16, 27)
aboveTwenty = 0
for temp in temperatures:
    if temp > 20:
        aboveTwenty += 1
    if temp >= 25:
        print("Hot!")
    elif temp >=18 and temp <= 24:
        print("Moderate!")
    elif temp < 18:
        print("Cold!")
    print(temp)
print("Temperature above twenty: ", aboveTwenty)