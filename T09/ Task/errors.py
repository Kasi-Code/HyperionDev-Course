# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# print "Welcome to the error program"
print("Welcome to the error program") # FIXED: Syntax Error - missing parentheses.

    # print "\n"
print("\n") # FIXED: Syntax Error - unexpected indentation and missing parentheses.

    # Variables declaring the user's age, casting the str to an int, and printing the result
    # age_Str == "24 years old." 
age_Str = "24" # FIXED: Syntax Error; Logical Error - unexpected indentation. Delete "years old." from string. Additionally, incorrectly used of comparsion "==" operator for "=" to assinged the variable. 

    # age = int(age_Str)
age = int(age_Str) # FIXED: Syntax Error - unexpected indentation.

    # print("I'm" + age + "years old.")
print("I'm " + str(age) + " years old.") # FIXED: Syntax Error; Runtime Error; Logical Error - unexpected indentation. Convert integer to string with str(). Need space " " in string beetween the age to correctly pritnt the sentence.  


    # Variables declaring additional years and printing the total years of age
    # years_from_now = "3"
years_from_now = 3 # FIXED: Syntax Error; Runtime Error - unexpected indentation. Changed variable from string to integer.

    # total_years = age + years_from_now
total_years = age + years_from_now # FIXED: Syntax Error -  unexpected indentation.

# print "The total number of years:" + "answer_years"
print("The total number of years: " + str(total_years)) # FIXED: Syntax Error; Runtime Error; Logical Error - missing parentheses. Changed sting to variable and convert it from integer to string with str().


# Variable to calculate the total amount of months from the total amount of years and printing the result
# total_months = total * 12
total_months = (total_years * 12) + 6 # FIXED: Runtime Error; Syntax Error - correctly name the chosen variable for the year. Needed extra six months extra.

# print "In 3 years and 6 months, I'll be " + total_months + " months old"
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old.") # FIXED: Syntax Error; Runtime Error; Logical Error - missing parentheses. Changed sting to variable and convert it from integer to string with str().

#HINT, 330 months is the correct answer


