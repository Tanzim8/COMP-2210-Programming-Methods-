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