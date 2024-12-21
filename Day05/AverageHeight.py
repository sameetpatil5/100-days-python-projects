student_heights=input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)

average_height=0
for i in range(0, len(student_heights)):
    average_height=average_height + student_heights[i]
print(round(average_height/len(student_heights)))

# Other Approch
total_height=0
for height in student_heights:
    total_height+=height
print(f"Total Height of all students is {total_height}")

number_of_students=0
for students in student_heights:
    number_of_students+=1
print(f"Number of students are {number_of_students}")

average_height=round(total_height/number_of_students)
print(average_height)

