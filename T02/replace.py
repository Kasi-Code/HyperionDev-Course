"""
Practical Task 2
Follow these steps:

● Create a new Python file in this folder called replace.py.

● Save the sentence: 

“The!quick!brown!fox!jumps!over!the!lazy!dog.” as a
single string.

○ Reprint this sentence as “The quick brown fox jumps over the lazy
dog.” using the replace() function to replace every “!” exclamation
mark with a blank space.

○ Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER
THE LAZY DOG.” using the upper() function

○ Reprint the sentence in reverse.

"""

# Given string

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Remove "!" from the string.

replace_sentence = sentence.replace("!", " ")

print(replace_sentence)

# Make the string all uppercase.

upper_sentence = replace_sentence.upper()

print(upper_sentence)

#  Reverse the strings.

reverse_sentence_low = replace_sentence[::-1]
reverse_sentence = upper_sentence[::-1]

print(reverse_sentence_low)
print(reverse_sentence)