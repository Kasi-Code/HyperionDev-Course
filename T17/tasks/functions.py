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


def arranged_task_index(task_index):
    tasks_dic = {}
    for i,t in enumerate(task_index):
        tasks_dic.update({i:t}) 
    
    # print(tasks_dic)

    tasks = []
    for key, value in tasks_dic.items():
        if key > 0:
            tasks = value
            due_date = value[85:95]
            # print(f"{key}: {value}")
            num_dic = {0: 123, 1: 5, 2: 6, 3: 75}

            # Use sorted to create a list of (key, value) tuples sorted by the values
            sorted_items = sorted(num_dic.items(), key=lambda x: x[1])

            # Create a new dictionary from the sorted list of tuples
            sorted_dic = dict(sorted_items)

            # print(sorted_dic)

            print(f"{tasks}")

    # filtered_dict = {key: value for key, value in tasks_dic.items() if key > 0}

    # print(filtered_dict)