"""
Practical Task 2
Follow these steps:

● Create a new Python file in the Dropbox folder for this task, and call it details.py.

● As in practical task 1, please first provide pseudo code as comments in your Python file, outlining how you will solve this problem.

● Use an input() command to get the following information from the user.

○ Name ○ Age
○ House number
○ Street name

● Print out a single sentence containing all the details of the user.

● For example:
This is John Smith. He is 28 years old and lives at house number 42 on Hamilton Street.

"""

# Here are string variables that can be use to construct sentances. From this, the code could be reuse to help reduce writting the code.

greeting = "Hi there! "
ask_user_for = "What is your "
name = "name? "
age = "age? "
house_num = "house number? "
street_name = "street name? "

# Here, the input asks the user to type their details by using global variables to construct the questions and automatically store the data as a varible for further uses.

name_input = input(f"{greeting}{ask_user_for}{name}").capitalize()
age_input = input(f"{greeting}{ask_user_for}{age}")
house_num_input = input(f"{greeting}{ask_user_for}{house_num}")
street_name_input = input(f"{greeting}{ask_user_for}{street_name}").capitalize()

# Here, a variable hold a sentence which are constructed with variables of the details that the user input from the questions.

single_sentence = f"This is {name_input}. I am {age_input} years old and lives at house number {house_num_input} on {street_name_input}."

# This will excute the code.

print(single_sentence)