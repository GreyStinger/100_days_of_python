# -*- Encoding: UTF-8 -*-

student_heights = input("Input a list of student heights divided with a comma and a space.\n: ").split(", ")

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

student_heights_added = 0

for students in student_heights:
    student_heights_added += students

average_height = student_heights_added // n

print(average_height)
