semester = int(input("Enter current semester number: "))
iteration = 0
totalCredits = 0
totalGradePoints = 0
while(iteration<semester):
    courseQuantities=int(input("Enter number of courses: "))
    for course in range(courseQuantities):
        credit=int(input("Enter Credit: "))
        totalCredits += credit
        grade=input("Enter letter grade: ")
        converted_grade=convert_grade(grade)
        gpa = converted_grade*credit
        totalGradePoints+=gpa

    iteration+=1;



def convert_grade(letter_grade):
            match grade:
                case "A+":
                    return 4.33
                case "A": 
                    return 4.0
                case "A-":
                    return 3.67
                case "B+":
                    return 3.33
                case "B":
                    return 3.0
                case "B-":
                    return 2.67
                case "C+":
                    return 2.33
                case "C":
                    return 2.00
                case "C-":
                    return 1.67
                case "D":
                    return 1.0
                case _:
                    print("Invalid letter grade.")
