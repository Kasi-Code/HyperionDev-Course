"""
Practical Task 1
Follow these steps:

● Create a new Python file in this folder called pattern.py.

● Write code to output the star pattern shown below, using an if-else statement in combination with a single for loop (it’s really easy with two, but using only one takes a little more thought!):
*
** 
*** 
**** 
***** 
**** 
*** 
**
*
"""

# Sets global variables

stars = "******"

star = ""

# The (len) will generate the index number and the (for) loop will iterate through its range.
# The loop will append each "*" to the variable depending on the index number.
# Then it'll print the amounth of "*" given. 

for i in range(len(stars)):

    star += "*"

    print(star)

    # The (if) statement will then print the reverse - as requested by the task.
    # The statement will subtract "*" one by one.

    if i == 5:

        star = star[:-1]
        star2 = star[:-2]
        star3 = star[:-3]
        star4 = star[:-4]
        star5 = star[:-5]

        print(star)
        print(star2)
        print(star3)
        print(star4)
        print(star5)

        break
