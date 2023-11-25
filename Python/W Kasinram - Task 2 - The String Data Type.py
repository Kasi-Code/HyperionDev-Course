name = str(input("Please enter your name: "))
age = input("How old are you? ")
age_str = str(age)

cap_name = name.capitalize()

greeting = f"+++Hello,There {cap_name}! You are {age_str} years old.+++++++"

index_to_lower = 9

greeting = greeting[:index_to_lower] + greeting[index_to_lower].lower() + greeting[index_to_lower + 1:]

greeting = greeting.strip("+")

greeting = greeting.replace(",", " ")

print(greeting)

greeting_list_of_words = greeting.split(" ")
greeting_index = len(greeting_list_of_words)

print(greeting_list_of_words, greeting_index)

name_from_list = greeting_list_of_words[2].strip("!")

nationality = str(input("What nationality are you " + name_from_list + "? ")).capitalize()

print(f"So you are {nationality}!")

select_you = greeting[18:21].lower()

question = str(input(f"Give me an adjective that spring to {select_you}r mind: "))

answer = f"You are feeling {question} right now..."

print(answer)

# Reverse 

reverse_greeting = greeting[::-1]

playing = f"""I just want to confuse you with this: {reverse_greeting} \n
           What do you think happened here {name_from_list}?"""

print(playing)

your_answer = str(input(" "))

print(f"So you think that \"{your_answer}\"...? Hmm...")