"""
Practical Task 1
Follow these steps:

● Create a file called alternative.py

● Write a program that reads in a string and makes each alternate character into an upper case character and each other alternate character a lower case character.

e.g. The string “Hello World” would become “HeLlO WoRlD”

● Now, try starting with the same string but making each alternative word
lower and upper case.

e.g. The string: “I am learning to code” would become “i AM learning
TO code”.

Tip: Using the split() and join() functions will help you here.

"""

# Strings given.

string = "Hello World"
string_1 = "I am learning to code"      

# The (while) loop will store the words/characters in the empty variables.
# The string will get "split" into words.
# The (while) loop will iterate through - depending on the index of the words/char.
# Inside, the (if) statement will append each alternative words/char as lower and upper case.
# Finally, the (join) statement will stitch the list into a string sentence.

str_list = []
characters = string
i = 0
while i < len(characters):
    if i % 2 == 1:
        str_list.append(characters[i].lower())
    else:
        str_list.append(characters[i].upper())
    i += 1
print("".join(str_list))

list_str = []
words = string_1.split(" ")
i = 0
while i < len(words):
    if i % 2 == 0:
        list_str.append(words[i].lower())
    else:
        list_str.append(words[i].upper())
    i += 1
print(" ".join(list_str))
