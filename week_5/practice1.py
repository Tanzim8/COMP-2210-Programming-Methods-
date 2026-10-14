#Dictionary
CanadaP = {"BC":"British Columbia",
           "QC":"Quebec",
           "AB":"Alberta",
           "ON":"Ontario"}
print(CanadaP)

#Specific
print(CanadaP["QC"])
CanadaP["NB"]="New Brunswick"
print(CanadaP)
del CanadaP ["AB"]
print(CanadaP)

temp = CanadaP.pop("ON")
print(temp)
print(CanadaP)

print("NB" in CanadaP)
print("ON" in CanadaP)

for shortQuotes in CanadaP:
    print(shortQuotes)

for values in CanadaP.values():
    print(values)

for codes, values in CanadaP.items():
    print(codes, "-r", values)

str1 = "We will have an exam on Monday at 8:30am"
str1words = {}
tempInt = 0

for words in str1.split():
    tempInt = tempInt +1
    str1words[words] = str1words.get(words, 0)+1
print(str1words)