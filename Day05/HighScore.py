student_scores=input("Input a list of students score").split()
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

max=0
for score in range(0, len(student_scores)):
    if int(student_scores[score])>int(max):
        max=student_scores[score]
print(f"The highest score in the class is: {max}")