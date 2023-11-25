"""
Practical Task 3
Follow these steps:

● Create a new Python file in this folder called conversion.py

● As in the previous practical tasks, please first provide pseudo code as
comments in your Python file, outlining how you will solve this problem.

● Declare the following variables:
○ num1 = 99.23
○ num2=23
○ num3=150
○ string1 = “100”

● Convert them as follows:
○ num1 into an integer
○ num2 into a float
○ num3 into a String
○ string1 into an integer

● Print out all the variables on separate lines

"""

# Variables given. 

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# Coverting variables to the type requested by using the build-in functions from Python. 

convert_num1 = int(num1)
convert_num2 = float(num2)
convert_num3 = str(num3)
convert_string1 = int(string1)

# Prints each variables on different line.

print(convert_num1)
print(convert_num2)
print(convert_num3)
print(convert_string1)

"""
# Here, we can check the variable's data type.

type_num1 = type(convert_num1)
type_num2 = type(convert_num2)
type_num3 = type(convert_num3)
type_string1 = type(convert_string1)

print(type_string1)

# Less coding but it does not print on different line.

print(convert_num1, convert_num2, convert_num3, convert_string1)

"""