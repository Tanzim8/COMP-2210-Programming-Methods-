def numSquare():
    num1 = 5
    num2 = num1*num1
    print("The Squere of the number is: ",num2)

numSquare()
def numSqcQue():
    num1 = 5
    if(num1%2 !=0):
        print("Number is not even", num1)
    else:
        print("Number is even", num1)
numSqcQue()

def numCheck(num1):
    if(num1%2 ==0):
        print(num1,"Number is even")
    else:
        print(num1, "Number is odd")

numCheck(11)
numCheck(16)

num2 = int(input("Enter a number: "))

numCheck(num2)

#returning some values
def addNum(num1, num2):
    num3 = num1+num2
    print("Addition of",num1,"and",num2,"is",num3)
    return num3
addNum(24,25)

num1 = int(input("Enter a number: "))

if num1 >=10 : 
    print(num1, "is bigger than 10")
    if num1 > 20: 
        print(num1, "is also bigger than 20")

if num1 >1 and num1<10:
    print(num1,"is greater than 1 and less than 10")
else:
    print(num1,"is not greater than 1 and less than 10")


def greetings(course="Advanced Coding", section="2031"):
    return "Welcome to ", course, "section: ", section, ", you will have a good time!"

print(greetings())

print(greetings("Programming methods", "2"))

courseName = "Capstone project"
courseID = "81"
print(greetings(courseName, courseID))

def divNums (num1, num2):
    if num2 == 0:
        return
    else:
        return num1/num2;
print(divNums(34,23))

def area(r):
    pi = 3.14
    return pi*r*r

print(area(4))
# print(r)

temp1 = 5
temp2 = 10

#python works for both floats and intigers
print(temp1+5, temp2-2.5)

import math
print(math.sqrt(temp1))

myList = [1, 10, 19, 56, 78]

for val in myList:
    print(val)

food = input("Enter a food name: ")

match food:
    case "pizza":
        print("Pizza in lunch")
    case "burger":
        print("Burger in lunch")
    case "":
        print("Nothing")

myName = "Tanzim Rahman"
print(len(myName))
print(myName[10])
print(myName[7:])

tempName = ""

for i in range(len(myName)):
    tempName = tempName + myName[-i-1]
print(tempName)