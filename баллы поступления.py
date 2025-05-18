points = 0

pl_test = int(input("Please write your polish test result: "))
math_test = int(input("Please write your math test result: "))
languege_test = int(input("Please write your language test result: "))
pl_assessment = int(input("Please write yuor polish assessment: "))
math_assessment = int(input("Please write yuor math assessment: "))
english_assessment = int(input("Please write yuor english assessment: "))
inf_assessment = int(input("Please write yuor informatyk assessment: "))

#test result
points += pl_test * 0.35
points += math_test * 0.35
points += languege_test * 0.3

# assessment
def pl_points():
    global points
    if pl_assessment == 1:
        points += 0
    elif pl_assessment == 2:
        points += 2
    elif pl_assessment == 3:
        points += 8
    elif pl_assessment == 4:
        points += 14
    elif pl_assessment == 5:
        points += 17
    elif pl_assessment == 6:
        points += 18
def math_points():
    global points
    if math_assessment == 1:
        points += 0
    elif math_assessment == 2:
        points += 2
    elif math_assessment == 3:
        points += 8
    elif math_assessment == 4:
        points += 14
    elif math_assessment == 5:
        points += 17
    elif math_assessment == 6:
        points += 18
def eng_points():
    global points
    if english_assessment == 1:
        points += 0
    elif english_assessment == 2:
        points += 2
    elif english_assessment == 3:
        points += 8
    elif english_assessment == 4:
        points += 14
    elif english_assessment == 5:
        points += 17
    elif english_assessment == 6:
        points += 18
def inf_points():
    global points
    if inf_assessment == 1:
        points += 0
    elif inf_assessment == 2:
        points += 2
    elif inf_assessment == 3:
        points += 8
    elif inf_assessment == 4:
        points += 14
    elif inf_assessment == 5:
        points += 17
    elif inf_assessment == 6:
        points += 18
pl_points()
math_points()
eng_points()
inf_points()
print(f"Your points: {points}")