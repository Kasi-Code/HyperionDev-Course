"""
Practical Task
● Create a new Python file in the Dropbox folder for this task, and call it dob_task.py.
● In your Python file, write a program that reads the data from the text file provided (DOB.txt) and prints it out in two different sections in the format displayed below:
Name
Orville Wright Rogelio Holloway Marjorie Figueroa ... etc.
Birthdate
21 July 1988
13 September 1988
 
9 October 1988 ... etc.

"""

import copy, re

contents = ""                           # Store the contents
copy_contents = ""
split_contents = []
split_line = []
split_details = []

with open("DOB.txt", "r+", encoding="utf-8") as file: # Open the file

    for line in file:                   # Iterate through the lines

        contents += line      # Add the contents of each line print(contents)  

    # print(split_line)                     # Print the contents


copy_contents = str(copy.deepcopy(contents.replace("\n", " ")))
split_line += re.split(" ", copy_contents)

cleaned_list = []

for item in split_line:
    if item:
        cleaned_list.append(item)

# print(cleaned_list)

# index = 0

firstname = []
lastname = []
day = []
month = []
year = []

for i in range(1, len(cleaned_list), 5):
    
    firstname.append(cleaned_list[i - 1])
    lastname.append(cleaned_list[i])
    day.append(cleaned_list[i+1])    
    month.append(cleaned_list[i+2])  
    year.append(cleaned_list[i+3])  

# print(firstname, lastname)

# DOB_dic = {k:v for k, v in zip(month, day)}
# px_dic = {}

# index = 0

# while index < len(day):

#     all_dob = [("Day", day[index])]
    
#     all_dob = dict(all_dob)
 
# px_dic = []

# kv_list = [(1, "hello"), (2, "dfvdf"), ("id", 4893829), (9, "fbff")]

# kv_list = dict(kv_list)

print(month)