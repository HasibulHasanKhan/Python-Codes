def is_passing(grade):
    return grade >= 70

grades = [33, 77, 87, 33, 36, 9, 65, 71]

# passsing_grade = list(filter(is_passing, grades))
passsing_grade = list(filter(lambda grade: grade >= 70, grades))

print(passsing_grade)