std_grades = [("Tanzim","COMP-3500", 88.5), 
             ("Tanzim", "COMP-2300", 78.5),
             ("Tanzim","ANTH-1100", 95),
             ("Tanzim", "SCIE-1400", 89),
             ("Hasan", "Math-1700", 99),
             ("Juliya", "ENGL-1100", 88)
             ]

gradesBook = {}

for std_name, std_subject, std_score in std_grades:
    if std_name not in gradesBook:
        #A list is required because I am storing multiple scores under one students name
        gradesBook[std_name] = []
    gradesBook[std_name].append(std_score)
for code,values in gradesBook.items():
    scoreTotal = 0
    scoreCount = 0
    # print(code,values)
    for score in values:
        scoreTotal += score
        scoreCount += 1
    print(code,"Score Average: ", scoreTotal/scoreCount)
