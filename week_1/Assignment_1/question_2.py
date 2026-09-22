#Name: M Tanzim Rahman
#ID-T00716893
#Course- COMP-2210
#Assignment_1
#Q-2

#Taking 5 inputs as the assignment required
f_Name = input("Enter your first name: ")
l_Name = input("Enter your last name: ")
std_ID = input("Enter your student id: ")
birth_Year = input("Enter your birth year: ")
birth_Country = input("Enter your birth country: ")

#concatinating all the 5 strings into 1 string
full_Info = f_Name+l_Name+std_ID+birth_Year+birth_Country
#Initializing a counter for the letter count
letterCount = 0

#using a for loop to iterate through the string which contains all the info all together also incrementing the counter
for ch in full_Info:

    #if only letters are suppossed to be counter ch.isalpha can be used inside a if statement
    letterCount+=1

# print(full_Info)

#printing the work
print("Total number of letters: ", letterCount)
print(f_Name[0],f_Name[-1], "\n", l_Name[0], l_Name[-1] ,"\n" , std_ID[0], std_ID[-1], "\n", birth_Year[0], birth_Year[-1], "\n", birth_Country[0], birth_Country[-1])