nums = []
total = 0
totalCounter = 0
listLenght = int(input("Enter list size: "))
while len(nums)!=listLenght:
    num = int(input("Enter number: "))
    nums.append(num)
    if num %2 == 0:
        total+=num
        totalCounter+=1
print("The list is: ",nums)
# print(total)
# print(totalCounter)
if totalCounter >0:
    average = total/totalCounter
    print("The average of all the even numbers in the list is: ", average)
else:
    print("There is no even number in the list.")
