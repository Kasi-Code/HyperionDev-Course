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

# An empty (list) of variables for IDs
# The (open) function will generate a new (txt) file as "a" was deployed
# "a" allows new request to appened to an exiting txt file
# The program will ask user for the quantity of registrar
# Accordingly, the (for) loop will ask user for the ID - can be number and letter
# If letter, all will turned into (uppercase) and append to the list variable
# second (for) loop will iterate through the (list) and appened to the (txt) file

student_id = []

file = open("reg_form.txt", "a")
num_of_student = int(input(
    "\nHow many students are registering? "
    ))

print()

while True:

    print(f"Please enter the student ID {num_of_student} times.\n")

    for id in range(num_of_student):
        entered_id = (input(
            "Please enter the student ID number: "
            )).upper()
        student_id.append(entered_id)

    print(f"""\nThese are the new student ID you've entered: 
{', '.join(student_id)}

Please see the (reg_form.txt) for the results.\n""")

    for i in range(len(student_id)):
        file.write(
            f"Student ID: {student_id[i]} \t" 
            "................Sign\n")
    file.close()
    break
