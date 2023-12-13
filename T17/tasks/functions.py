import copy, re

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


def arrange_task_index (disp_str):
    index = 0
    user_tasks = []
    for i in disp_str:
        user_tasks.append(i)
    
    # print(user_tasks)