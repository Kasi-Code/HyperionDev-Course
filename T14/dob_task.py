"""
Practical Task
● Create a new Python file in the Dropbox folder for this task, and call it dob_task.py.
● In your Python file, write a program that reads the data from the text file provided (DOB.txt) and prints it out in two different sections in the format displayed below:

Name
Orville Wright 
Rogelio Holloway 
Marjorie Figueroa ... etc.

Birthdate
21 July 1988
13 September 1988
9 October 1988 ... etc.

"""

# Firstly, (import) was deployed to enable external functions
# Empty variables will be stored
# The (open) statemnent will fetch text from located folder
# The (for) loop will split lines and store text to the empty variables
# Then (copy) will make a copy of the text from the original

import copy, re

contents = ""                 # Store the contents
copy_contents = ""            # To maintain the original copy
split_contents = []
split_line = []
split_details = []

with open("IO Operations Input/tasks/DOB.txt", "r+", encoding="utf-8") as file: # Open the file

    for line in file:         # Iterate through the lines

        contents += line      # Add the contents of each line print(contents)  

copy_contents = str(copy.deepcopy(contents.replace("\n", " ")))
split_line += re.split(" ", copy_contents)

#  Additionally, this (for) loop will clear unwanted empty item generated

cleaned_list = []

for item in split_line:
    if item:
        cleaned_list.append(item)

#  Data will be stored to the empty (list) and (dictionary) variables
#  The (for) loop will iterate through the text and append each word accordingly
#  Data will be grouped in variable and dictionary separately

firstname = []
lastname = []
day = []
month = []
year = []

name_dic = {}
DOB_dic = {}
px_dic = {}

for i in range(1, len(cleaned_list), 5):

    firstname.append(cleaned_list[i - 1])
    lastname.append(cleaned_list[i])
    day.append(cleaned_list[i+1])    
    month.append(cleaned_list[i+2])  
    year.append(cleaned_list[i+3])  

    name_dic = [("First_name", firstname), ("Last_name", lastname)]
    name_dic = dict(name_dic)

    DOB_dic = [("Day", day), ("Month", month), ("Year", year)]
    DOB_dic = dict(DOB_dic)

    px_dic = [("First_name", firstname), ("Last_name", lastname), ("Day", day), ("Month", month), ("Year", year)]
    px_dic = dict(px_dic)

# The (for) loop will iterate through the (dictionaries) created
# Then, it'll generate strings for (Name) and (Birthdate) accordingly
# Finally, data will be printed 

print("\nName")

for v in range(len((px_dic["First_name"]))):

    FN = px_dic["First_name"][v]
    LN = px_dic["Last_name"][v]

    names = FN + " " + LN

    print(names)

print("\nBirthdate")

for v in range(len((px_dic["First_name"]))):

    DD = px_dic["Day"][v]
    MM = px_dic["Month"][v]
    YY = px_dic["Year"][v]

    DOBs = f"{DD} {MM} {YY}"

    print(DOBs)

"""
for v in range(len((px_dic["First_name"]))):

    FN = px_dic["First_name"][v]
    LN = px_dic["Last_name"][v]

    DD = px_dic["Day"][v]
    MM = px_dic["Month"][v]
    YY = px_dic["Year"][v]

    names = FN + " " + LN
    DOBs = f"{DD} {MM} {YY}"

    print(names)
    print(DOBs)

"""

