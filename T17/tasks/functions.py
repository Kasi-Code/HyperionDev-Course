import copy, re
from datetime import datetime

def reg_user(input_name):
    with open("user.txt", "r") as username_pass_list:
        user_contents = ""
        split_string = ""
        username = []
        for name in username_pass_list:
            user_contents += name.replace("\n", " ")
        split_string = str(copy.deepcopy(user_contents.replace(";", " ")))
        username += re.split(" ", split_string)

        names = []
        i = 0
        while i < len(username):
            if i % 2 == 0:
                names.append(username[i])
            i += 1

        if input_name in names:
            return False
        else:
            return input_name
            
def selecting_task_num(num_of_index):

    task_num = input(f"\nTask: {', '.join(map(str, num_of_index))}\n\nSelect task number: ")
    print()

    try:
        task_num = int(task_num)
        if task_num < 1 or task_num > len(num_of_index):
            print("Invalid task number. Please enter a valid task number.")
            return 0
        else:
            return task_num
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return 0

    