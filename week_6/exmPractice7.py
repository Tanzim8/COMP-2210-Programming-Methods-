students = [
    ("Ali", "COMP", 85),
    ("Sara", "MATH", 92),
    ("Ali", "MATH", 75),
    ("Sara", "COMP", 88),
    ("John", "COMP", 70)
]

# std_name , std_sub, std_score = students
# print(std_name)

new_students = {}
for std_name , std_sub, std_score in students:
    # print(std_name,std_sub,std_score)
    if std_name not in new_students:
        new_students[std_name] = []
    new_students[std_name].append(std_score)
    new_students[std_name] = new_students.get(std_name)
    # for std_name,std_score in new_students:
    #     print(new_students[std_name])
for code,values in new_students.items():
    total_score = 0
    score_count = 0
    for score in values:
        total_score += score
        score_count +=1
    print(code,"Score Average: ", total_score/score_count)
print(new_students)
