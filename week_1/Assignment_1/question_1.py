#Name: M Tanzim Rahman
#ID-T00716893
#Course- COMP-2210
#Assignment_1

#Initializing an empty list
nums = []
#Initializing a variable that will store the even values from the list
total = 0
#Initializing a counter which will only increment when there is a even number in the list
totalCounter = 0
#Asking the user about the list size
listLength = int(input("Enter list size: "))
#Using a while loop to ask the user to enter number till the lenght user entered earlier and storing it in the list
while len(nums)!=listLength:
    num = int(input("Enter number: "))
    #storing in the list using append
    nums.append(num)
    #checking if the number is even or not if even adding it in the total variable
    if num %2 == 0:
        total+=num
        #incrementing the total counter
        totalCounter+=1
#printing the list
print("The list is: ",nums)
# print(total)
# print(totalCounter)

#Printing the list depending on the totalCounter
if totalCounter >0:
    average = total/totalCounter
    print("The average of all the even numbers in the list is: ", average)
else:
    print("There is no even number in the list.")
