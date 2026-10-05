str = " Ganzafar Latif"
digits = "123456"
str2 = "Latif"
myList = [1,2,3,4,5,6]
if str.startswith("G") and str.endswith("f"):
    print("Name starts with G ends with f.")
else:
    print("Name doesnt starts with F and ends with f. ")

print(str.isalpha())
print(digits.isdigit())
print(str.find("z"))
print(str.lower())
print(str.upper())
#removes spaces in th ebegining and the end
print(str.strip())
print(str.replace("a", "A"))
print(str.split("a"))
print(str.join(digits))
print(str.join(str2))

marks = 97.563
print(str,digits)
print(f"[str] recieved scores of {marks}")
print(f"[str] recieved scores of {marks:.1f}")
print(f"{str2:>10}| {marks:6.2f}")

print(myList)
for i in myList: 
    print(i)
myList.append(11)
print(myList)
myList.insert(2,4)
print(myList)

myList.remove(4)
print(myList)
print(myList.pop(0))
print(myList)

del myList[0]
print(myList)

myList2 = [13, 15, 17]
myList3 = myList + myList2
print(myList3)

myList4 = [13,16,18]
if myList4 == myList2:
    print("Both have same values.")
else:
    print("lists are not equal.")
print(myList2 in myList4)
print(myList3 is myList)

myList4.sort()
print(myList4)

myList5 = sorted(myList4, reverse=True)
print(myList5)

myCourses = [
    ["COMP 2210","Programming Methods", "Ganzafar Latif"],
    ["COMP 4910", "Capstone Project", "Ganzafar Latif"],
    ["COMP 3540", "Advanced Web Programming", "Ganzafar Latif"],
]
print(myCourses)
print(myCourses[0][:])
print(myCourses[0][0])
print(myCourses[:][0])