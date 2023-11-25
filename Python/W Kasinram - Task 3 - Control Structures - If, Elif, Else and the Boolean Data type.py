pizza = True
code = 1234
cost = 5.00
card = "Card"
cash = "Cash"

if pizza != False:

    print(f"Your pizza is ready. It's £{cost}, would you like to pay with Card or Cash? ")
    user_input = str(input("")).capitalize()

    if user_input == card:

        pin_num = int(input("Please type in your 4 digits number: "))

        if pin_num == code:

            print("Here's your pizaa. Thank you!")

        else:

            print("Error! Please try again: ")
            pin_num = int(input("Please type in your 4 digits number: "))

            if pin_num != code:

                print("Please start again.")
    
    elif user_input == cash:

        print("How much is that? ")
        cash_amount = float(input(""))

        if cash_amount == cost:

            print("Here's your pizaa. Thank you!")

        elif cash_amount < cost:

            amount_left_to_pay = cost - cash_amount

            print(f"£{cash_amount} You don't have enough cash! I need £{amount_left_to_pay} more please")  

        else:
        
            amount_left_to_pay = cash_amount -cost

            print(f"£{cash_amount}, here's your change £{amount_left_to_pay}.")

    else:

        print(f"I only accept {cash} or {card}.")
                