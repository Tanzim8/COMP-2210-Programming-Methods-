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