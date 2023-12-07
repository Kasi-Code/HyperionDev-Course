"""
Practical Task 2

● Write a program that displays a logical error (be as creative as possible!).

"""

# The program suppose to ask user to enter numbers in mind.
# Then ask for the percentage.
# Lastly, it should add all the numbers and calculate the percentage of it.

print("Hi, I will add the number(s) you give me, and work out its percentage for you!")

name = input("First of all, what's your name? ") # Logical error: If user type (lowercase), program won't correct the first charactor to (capital). 

total = 0
num_list = []

input_num = int(input(f"Hi{name}! Please type the number. If you put (0) then I will stop: ")) # Logical error: No space between "Hi" and the (name) variable.

while input_num != 1: # Logical error: Comparison assinged to (1) instead of (0).

    total += input_num
    num_list.append(input_num)

    input_num = int(input("Please type the number. If you put (0) then I will stop: "))

    if input_num == 1: # Logical error: Comparison assinged to (1) instead (0).

        percent = int(input("Waht is the percentage? "))

        percentage = total / percent # Logical error: suppose to turn number given into decimal first.

        total = str(round(total, 2))
        num_list = str(num_list).replace("[", "").replace("]", "")

        print(f"\nThe number you entered: {num_list}.\n\n{percent}% of {total} is {percentage}!\n") # As a result, the number calculated is incorrect. 
        
        break