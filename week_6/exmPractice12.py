grades = [
    ("Ali", 80),
    ("Sara", 90),
    ("Ali", 70),
    ("Sara", 100)
]
grade_book = {}

for std_name, std_grade in grades:
    if std_name not in grade_book:
        grade_book[std_name] = []
    grade_book[std_name].append(std_grade)
for code, values in grade_book.items(): 
    score_total = 0
    score_count = 0

    for scores in values: 
        score_total += scores
        score_count += 1
    print(code,": ",score_total/score_count)

print(grade_book)