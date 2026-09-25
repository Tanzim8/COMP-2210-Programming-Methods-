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