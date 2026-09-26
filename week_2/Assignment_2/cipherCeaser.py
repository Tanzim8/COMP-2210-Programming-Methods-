# Assignment2, Q-1
#Name: M Tanzim Rahman
#ID-T00716893
#COMP-2210
#Reference: 
#1. https://www.geeksforgeeks.org/ethical-hacking/caesar-cipher-in-cryptography/
# I looked up for the exact formule that is needed to use to convert the characters into ascii value and than add the shift value and i found it up on the website I sitet
userInput = input("Enter a string: ")
userShiftVal = int(input("Enter shift value: "))

def encode(userInput, userShiftVal):
    finalUserInput = ""
    for char in userInput:
        if char.isupper(): 
            userInputAltered = (ord(char) - ord('A') + userShiftVal) % 26 + ord('A')
            # print(userInputAltered)
            finalUserInput += chr(userInputAltered)
        elif char.islower():
            userInputAltered = (ord(char) - ord('a') + userShiftVal) % 26 + ord('a')
            # print(userInputAltered)
            finalUserInput += chr(userInputAltered)
        # print(finalUserInput)
    return finalUserInput
# print(encode(userInput, userShiftVal))
encodedStr = encode(userInput, userShiftVal)
print("Encoded: ",encodedStr)

def decode(inputSecret, userShiftVal):
    finalOrginal = ""
    for char in inputSecret:
        if char.isupper():
            secretAltered = (ord(char) - ord('A') - userShiftVal)%26 + ord('A')
            finalOrginal+= chr(secretAltered)
        elif char.islower():
            secretAltered = (ord(char) - ord('a') - userShiftVal)%26 + ord('a')
            finalOrginal += chr(secretAltered)
    return finalOrginal
print("Decoded: ", decode(encodedStr, userShiftVal))


