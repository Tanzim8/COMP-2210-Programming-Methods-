userString1 = input("Enter first string containing numbers and strings: ")
userString2 = input("Enter second string containing numbers and strings: ")

numStr1 = ""
numStr2 = ""
l1 = []
l2 = []

# print(final)

for char in userString1:
    if char.isdigit():
        numStr1 +=char
    else:
        l1.append(char)
# print(l1)
# print(numStr1)

for char in userString2:
    if char.isdigit():

        numStr2 +=char
    else:
        l2.append(char)
# print(l2)
# print(numStr2)
finalNum = int(numStr1) + int(numStr2)
# print(finalNum)
finalList = []
finalList.append(finalNum)
finalList.append(l1+l2)
# finalList.append(l2)
print(finalList)