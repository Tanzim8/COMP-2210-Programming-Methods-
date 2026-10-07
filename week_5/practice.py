#will practice tuples here
point = (3,4)
triple = 1,2,3
single = (42,)
empty = ()

point[0]
len(triple)
# point[0] = 9

myTuple = (1,3,5,7,9)
print(myTuple)
myTuple2 = 1,3,5,7,9

print(myTuple2)

myTuple3 = 45,
print(myTuple3)

myTuple4 = ()
print(myTuple4)

print(myTuple[2])

print(len(myTuple))
print(len(myTuple3))
# myTuple[2] = 11
# myTuple.append(11)

myTuple5 = (11,13)
x,y = myTuple5
print(x)
print(y)

x,y = y,x

print(x)
print(y)

# myList = [7,14,3,9,12]
def minMax(myList):
    low = min(myList)
    high = max(myList)
    return(low,high)

myList = [7,14,3,9,12]

minMaxCalc = minMax(myList)
print(minMaxCalc)

l,h = minMax(myList)
print("Low: ", l, "High: ", h)

myInfo = ["Tanzim", "Rahman", 97.5]

lastName, firstName, grade = myInfo
print(lastName, firstName, grade)

courseID = ["COMP 2210", "COMP2920", "COMP3590", "COMP4123"]
courseName = ["P. Methods", "Adv Prgmming", "Network Secutry", "UNix Tools"]

for id, name in zip(courseID, courseName):
    print(id,name)

for i, id in enumerate(courseID):
    print(i, id)