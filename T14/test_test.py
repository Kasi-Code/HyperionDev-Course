import copy, re

contents = ""                           # Store the contents
copy_contents = ""
split_contents = []
split_line = []
split_details = []

with open("DOB.txt", "r+", encoding="utf-8") as file:


    for line in file:                   # Iterate through the lines

        contents += line   