# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# animal = Lion
animal = "Lion" # FIXED: Runtime Error; - missing quotations for the string.
animal_type = "cub"
number_of_teeth = 16

# full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth." # FIXED: Logical error - missing "f" in front of the quotation when embedding expressions in F-Strings. 

# print full_spec
print(full_spec) # FIXED: Syntax Error; - missing parentheses.

