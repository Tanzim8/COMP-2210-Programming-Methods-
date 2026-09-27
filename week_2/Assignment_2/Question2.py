# Assignment2, Q-2
#Name: M Tanzim Rahman
#ID-T00716893
#COMP-2210
#Reference: 
# 1. https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend
# 2. https://www.geeksforgeeks.org/python/split-elements-of-a-list-in-python/
userInput1 = input("Enter first string containing numbers and strings: ")
userInput2 = input("Enter second string containing numbers and strings: ")

#Looked up online and got to know about this tool to specifically split list items based on condition
words1 = userInput1.split()
words2 = userInput2.split()

# print(words1)
# print(words2)

l1 = []
l2 = []
finalNum =0
for item in words1:
    if item.isdigit():
        # l1.append(int(item))
        finalNum+=int(item)
    else:
        l1.append(item)

for item in words2:
    if item.isdigit():
        # l2.append(int(item))
        finalNum +=int(item)
    else:
        l2.append(item)

# print(l1)
# print(l2)

finalList = []
# finalList.append(str(finalNum)+l1+l2)
finalList.append(finalNum)
#without extend the list was having brackets in between when i was appending both list and the number so i used extend, I looked up online for this specific issue that I was encoutering
finalList.extend(l1+l2)
print(finalList)