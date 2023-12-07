"""
Challenge
Use this opportunity to extend yourself by completing an optional challenge activity.
Follow these steps:
● Create a new Python file called optional_challenge.py.
● Write a program with two compilation errors, a runtime error and a logical error.
● Next to each error, add a comment that explains what type of error it is and why it occurs.

"""

# This program suppose to ask user to input the number in mind for 5 times.
# Then it should select the second number the user inputted.

print("Give me 5 numbers and I will select the second number you gave me!")

num_input = int(input("What number do you have in mind? "))

total = 0
num_list =  "" # Synthtax error: empty string ("") was deployed instead of list ([]). 

while total < 4:  

    total = 1 # Logical error: the total won't add up as the (+) operator is missing in front of (=).
    num_list.append(num_input)

    num_input = int(input("What number do you have in mind? "))

    if total == 4:

        list_result = num_list.replace("[", "").replace("]", "") # Synthtax error: the (num_list) variable must be converted to str() first.

        print(f"\nThe number you entered: {list_result}.\n\nThe 2nd number you entered is {num_list[2]}") # Runtime error: The string printed the third (index) intead of the second as mentioned because the index starts from (0). 
        
        break