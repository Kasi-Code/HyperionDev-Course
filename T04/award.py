"""
Practical Task 1
Follow these steps:
● Create a new Python file in this folder called award.py.
● Design a program that determines the award a person competing in a
triathlon will receive.
● Your program should read in the times (in minutes) for all three events of a
triathlon, namely swimming, cycling, and running, and then calculate and
display the total time taken to complete the triathlon.
● The award a participant receives is based on the total time taken to
complete the triathlon. The qualifying time for awards is 100 minutes. Display the award that the participant will receive based on the following criteria:

"""
ask_user = "The time in minute taken to complete"

swimming_time = int(input(f"{ask_user} swimming is: "))
cycling_time = int(input(f"{ask_user} cycling is: "))
running_time = int(input(f"{ask_user} running is: "))

triathlon_total_time = swimming_time + cycling_time + running_time

# print(triathlon_total_time)

first = f"Congratulations! The total time is {triathlon_total_time} minutes. This is an award of Provincial Colours!"

second = f"Great! The total time is {triathlon_total_time} minutes. This is an award of Provincial Half Colours!"

third = f"Well done! The total time is {triathlon_total_time} minutes. This is an award of Provincial Scroll."

fourth = f"You've finished! The total time is {triathlon_total_time} minutes. There is No award."

if triathlon_total_time <= 100:
    print(first)
elif triathlon_total_time > 100 and triathlon_total_time <= 105:
    print(second)
elif triathlon_total_time > 105 and triathlon_total_time <= 110:
    print(third)
else:
    print(fourth)