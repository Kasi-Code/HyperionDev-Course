"""
Practical Task
Follow these steps:

● Create a file called student_register.py

● Write a program that allows a user to register students for an exam venue.

● First, ask the user how many students are registering.

● Create a for loop that runs for that number of students.

● Each time the loop runs the program should ask the user to enter the
next student ID number.

● Write each of the ID numbers to a text file called reg_form.txt

● Include a dotted line after each student ID because this document will be
used as an attendance register, which the students will sign when they arrive at the exam venue.

"""

ID = []

num_of_student = int(input("How many students are registering? "))

for _ in range(num_of_student):

    student_id = int(input("Please enter the student ID number: "))
    ID.append(student_id)

    file = open("reg_form.txt", "a")

    file.write(f"{ID}")
    file.close()

print(ID)

