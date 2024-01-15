"""Capstone Project

For this Capstone Project, assume that you have been approached by 
a small financial company and asked to create a program that allows 
the user to access two different financial calculators: an investment 
calculator and a home loan repayment calculator."""

import math

# The program will first greet the user and ask for their name. 
# This will give a human touch. 
# Then user will need to select their chioce to "invest" or "bond".
# If the user typed an unregconised input, 
# the program will ask the user to start again.

user_name = input("""Hi and welcome to the AI-Banking!
                  
Here, we'll help you to calculate the amount of interest 
you'll earn on your investment, or to calculate the amount 
you'll have to repay on a home loan.
                  
First of all, what's your name? """).capitalize()

try:

    user_choice = int(input(f"""
        Hi {user_name}! What would you like to do? 
                            
        1. Investment
        2. Bond
        """))
    print()

    if user_choice == 1:
        input_amount = int(input(
            "Please enter the amount of money that you would like to deposit: "))
        input_interest = int(input(
            "Please enter the percentage of your interest rate: "))
        input_year = int(input(
            "Please enter the number of years you plan on investing: "))
        interest = int(input("""\nFinally, please select your interest:
                        
        1. Simple
        2. Compound
        """))

        # The calculation for Simple and Compound interests.
        # Then the if statement will compose and make sure that 
        # a final sentence of the result is a string, and print the output.

        if interest == 1:
            convert_to_percent = input_interest / 100
            interest_gained = input_amount * (1 + (convert_to_percent * input_year))
            interest_gained = interest_gained - input_amount  
            interest_gained = str(round(interest_gained, 2))
            
            result = f"""\nThank you for the information {user_name}!
            
    Here is the calculation of the Simple interest 
    for the amount of £{input_amount}; with an interest 
    of {input_interest}%; over {input_year} year(s).

    Total: £{interest_gained}\n"""

            print(f"{result}")

        elif interest == 2:
            convert_to_percent = input_interest / 100
            interest_gained = input_amount * math.pow((1 + convert_to_percent), input_year)
            interest_gained = interest_gained - input_amount 
            interest_gained = str(round(interest_gained, 2))

            result = f"""\nThank you for the information {user_name}!
            
    Here is the calculation of the Compound interest 
    for the amount of £{input_amount}; with an interest 
    of {input_interest}%; over {input_year} year(s).

    Total: £{interest_gained}\n"""

            print(f"{result}")

    elif user_choice == 2:
        house_value = int(input(
            "What is the present value of the house? "))
        input_interest = int(input(
            "What is the interest rate? "))
        input_month = int(input(
            "What is the number of months you plan to repay the bond? "))

        # The calculation for the Bond.
        convert_to_percent = (input_interest / 100) / 12
        repayment = (convert_to_percent * house_value)/(1 - (1 + convert_to_percent)**(-input_month))
        total_repayment = repayment * input_month
        total_repayment = str(round(total_repayment, 2))
        repayment = str(round(repayment, 2))

        result = f"""\nThank you for the information {user_name}!
        
Here is the calculation of how much money you will be 
repaying each month, if the value of the house is £{house_value}; 
with an interest of {input_interest}%; over {input_month} month(s).

    Total payment each month: £{repayment}
    Total repayment: £{total_repayment}\n"""

        print(result)

    else:

        print("""
    I'm sorry, that's not one of the options.
    Please try agian.""")
        
except ValueError:

    print("""
I'm sorry, that's not one of the options.
Please type number only.
Try agian.\n""")