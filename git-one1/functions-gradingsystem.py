def grading_system(score):
    '''this shows your grade according to your mark'''
    if score>=75:
        grade="A"
    elif score>=65:
        grade="B"
    elif score>=50:
        grade="C"
    elif score>=35:
        grade="S"
    else:
        grade="F"
    return(grade)

grade=grading_system(66)
print(grade)