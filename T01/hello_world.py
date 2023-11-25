"""
Practical Task 1
Follow these steps:

● Create a new Python file in the Dropbox folder for this task, and call it hello_world.py.

● First, provide pseudo code as comments in your Python file, outlining how you will solve this problem (you’ll need to read the rest of this practical task first of course!).

● Now, inside your hello_world.py file, write Python code to take in a user’s name using input() and then print out the name.

● Use the same input and output approach to take in a user’s age and print it out.

● Finally, print the string “Hello World!” on a new line (the new line will happen by default if you use a separate print statement to the one you used immediately above to print out the age, because each print statement automatically inserts an “enter”, or newline instruction, at the end).

"""

# The variable "user_name" stores what the user entered into the box as a string.
user_name = input("Please enter your name: ")

# The variable "user_age" stores what the user entered into the box as an integer.
user_age = int(input("Please enter your age: "))

# Here is where the first letter of the name will be captitalised.
user_name = user_name.capitalize()

# Here is where the integer will be converted to string becuase both interger and string cannot be executed together.
user_age = str(user_age)

#  Here are three ways you can print the statement by using the variables from the input. 
 
greeting = "Hello there " + user_name + " and you are " + user_age + " years old!"

greeting_2 = f"Hello there {user_name} and you are {user_age} years old!"

greeting_3 = "Hello there {} and you are {} years old!".format(user_name, user_age)

print(greeting)

# This will print "Hello World!" on a separate line. 

print("Hello World!")

# Now, this file is running, notice the output produced by the following command.