students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Nville": 62,
}

students_grades = {}

for student in students_scores:
    score = students_scores[student]
    if score > 90:
        students_grades[student] = "Outstanding"
    elif score > 80:
        students_grades[student] = "Exceeds Expections"
    elif score > 70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"

print(students_grades)