scores = [78, 92, 65, 88, 45, 95, 72, 60]
over_eighty = 0
over_sixty = 0
over_sixty_count = 0
maxScore = scores[0]
for score in scores:
    # print(score)
    if(score>=80 and maxScore < score):
        over_eighty+=1
        maxScore = score
    if(score>=60):
        over_sixty += score
        over_sixty_count += 1
        print(score, " - Pass!")
    else:
        print(score, " - Fail!")
print(maxScore)
print("Score over 80: ", over_eighty)
print("Average scores over 60: ", over_sixty/over_sixty_count)
