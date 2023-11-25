"""
Practical Task 1
Follow these steps:

● Create a file called while.py.

● Write a program that continually asks the user to enter a number.

● When the user enters “-1”, the program should stop requesting the user to enter a number,

● The program must then calculate the average of the numbers entered, excluding the -1.
 
● Make use of the while loop repetition structure to implement the program.

"""

# Global variables 

total = 0
quantity = 0
num_list = []

# The input asks user to type in the number and store it as a variable in integer.
# The while loop will keep asking for the numbers until user type (-1) - it'll stop.

input_num = int(input("Please type the number. If you put (-1) then I will stop: "))

while input_num != -1:

    total += input_num
    quantity += 1
    num_list.append(input_num)

    input_num = int(input("Please type the number. If you put (-1) then I will stop: "))

    # The (if) statement will calculate the average number when the user type (-1).
    # Finally, it'll print the message with all the number(s) entered; inclding an average number.
    # the "break" statement will make sure the function stop running - just incase of the infinate loop.

    if input_num == -1:

        # print(total, quantity, num_list)

        total = (total + 1) / quantity

        total = str(round(total, 2))
        num_list = str(num_list).replace("[", "").replace("]", "")

        print(f"\nThe number you entered: {num_list}.\n\nThe average numbers is {total}!\n")
        
        break