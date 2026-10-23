myFile = open("p1.txt","r")
data = myFile.read()
myFile.close()
print(data)

myFile2 = open("p1.txt", "a")
str = "We had exam this week wish all grade we will have Nov: 3"
myFile2.write(str)
myFile2.close()
myFile3 = open("p1.txt","a")
myFile3.write(str)
myFile3.close()
myFile4 = open("p1.txt", "a")
myFile4.write(str)

myFile4.close()

myFile5 = open("p1.txt", "r")
i = 1

for line in myFile5: 
    print("line number: ", i)
    i = i+1
    print(line)
    tempList = line.split()
    print(tempList)
    print("Why i am doing this ", tempList[2])
myFile5.close()