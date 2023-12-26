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

def view_edit_task(user_choice):
    tasks_dic = {}
    if isinstance(user_choice, list):
        for i, t in enumerate(user_choice):
            tasks_dic.update({i: t})

        # Create a list to store tuples of (task_key, due_date)
        task_due_dates = []

        # Extract due dates and convert them to datetime objects
        for key, value in tasks_dic.items():
            if key == 0:
                continue
            tasks = value
            due_date_str = tasks.find("Due Date:")
            sliced_date = slice(due_date_str + 13, due_date_str + 23)
            grabbed_due_date = tasks[sliced_date]
            due_date_obj = datetime.strptime(grabbed_due_date, "%Y-%m-%d")
            task_due_dates.append((key, due_date_obj))

        if task_due_dates:
            # Sort tasks based on due dates
            sorted_tasks = sorted(task_due_dates, key=lambda x: x[1])

            print("\nHere are your task(s) - please find the shortest due-date starting from the top!\n")

            # Print tasks in sorted order
            for task_key, _ in sorted_tasks:
                print(tasks_dic[task_key])

            print("\nHere are your task(s) - please find the shortest due-date starting from the top!\n")
            return tasks_dic
        else:
            print("\nYou do not have any task.\n")
            return False
    else:
        print(tasks_dic)

    
# def get_tasks_file(_):
#     with open("tasks.txt", 'r') as task_file:
#     task_data = task_file.read().split("\n")
#     task_data = [t for t in task_data if t != ""]

# def marked_task(status):
#     task_list = []
#     with open("tasks.txt", 'r+') as task_file:
#         for t in task_file:
#             for j in t:

#     task_data = task_file.read().split("\n")
#     task_data = [t for t in task_data if t != ""]
#                 print(j[0])