"""
Capstone Project

For this Capstone Project, assume that you have been approached by a small financial company and asked to create a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

"""

import math

# Repetition of words for this project.

keyword_invest = "Investment"
keyword_bond = "Bond"

#  The program will first greet the user and ask for their name. This will give a human touch. 
# Then user will need to select their chioce to "invest" or "bond".
# If the user typed an unregconised input, the program will ask the user to start again.

user_name = input("Hi and welcome to the AI-Banking!\n\nHere we'll help you to calculate the amount of interest you'll earn on your investment or to calculate the amount you'll have to pay on a home loan.\n\nFirst of all, what's your name? ").capitalize()

user_chioce = input(f"Hi {user_name}! Would you like to \"Investment\" or \"Bond\"? Please type: ").upper()


if (user_chioce == "INVESTMENT") or (user_chioce.__contains__("INVEST")):

    user_chioce = keyword_invest

elif (user_chioce == "BOND") or (user_chioce.__contains__("BOND")):
    
    user_chioce = keyword_bond


if user_chioce == keyword_invest:

    input_amount = int(input("Please enter the amount of money that you would like to deposit: "))
    input_interest = int(input("Please enter the percentage of your interest rate: "))
    input_year = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Finally, please type \"simple\" or \"compound\" for your interest: ").upper()

    # The calculation for Simple and Compound interests.
    # Then the if statement will compose and make sure that a final sentence of the result is a string, and print the output.

    if interest == "SIMPLE":

        convert_to_percent = input_interest / 100
        interest_gained = input_amount * (1 + (convert_to_percent * input_year))
        interest_gained = str(round(interest_gained, 2))
        
        result = f"Thank you for the information {user_name}!\n\nHere is the calculation of the Simple interest for the amount of £{input_amount} with an interest of {input_interest}% over {input_year} year(s).\n\nTotal: £{interest_gained}"

        print(f"{result}")

    elif interest == "COMPOUND":
        
        convert_to_percent = input_interest / 100
        interest_gained = input_amount * math.pow((1+convert_to_percent), input_year)
        interest_gained = str(round(interest_gained, 2))

        result = f"Thank you for the information {user_name}!\n\nHere is the calculation of the Compound interest for the amount of £{input_amount} with an interest of {input_interest}% over {input_year} year(s).\n\nTotal: £{interest_gained}"

        print(f"{result}")

    else:

        print("I'm sorry, we only recognise the \"simple\" or \"compound\" terms. Please try agian.")


elif user_chioce == keyword_bond:

    house_value = int(input("What is the present value of the house? "))
    input_interest = int(input("What is the interest rate? "))
    input_month = int(input("What is the number of months you plan to repay the bond? "))

    # The calculation for the Bond.

    convert_to_percent = (input_interest / 100) / 12
    repayment = (convert_to_percent * house_value)/(1 - (1 + convert_to_percent)**(-input_month))
    total_repayment = repayment * input_month
    total_repayment = str(round(total_repayment, 2))
    repayment = str(round(repayment, 2))

    result = f"Thank you for the information {user_name}!\n\nHere is the calculation of how much money you will have to repay each month if the value of the house is £{house_value} with an interest of {input_interest}% over {input_month} month(s).\n\nTotal to pay each month: £{repayment} \t Total repayment: £{total_repayment}"

    print(result)

else:

    print("I'm sorry we only calculate the amount of interest you'll earn on your investment or the amount you'll have to pay on a home loan. Please try agian.")