def factorialNum(num1):
    if num1 == 0:
        return 1
    else:
        print(num1)
        return num1*factorialNum(num1-1)

print("Final Result:", factorialNum(5))

def nSum(num2):
    if num2 <= 0:
        return 1
    return factorialNum(num2-1)+num2

print(nSum(5))

def sumTwoVar(num1, num2):
    if(num1 > num2):
        return 0
    if(num1 != num2):
        return num1 + sumTwoVar(num1+1, num2)
    else:
        return num2

print(sumTwoVar(0,20))
print(sumTwoVar(25, 35))