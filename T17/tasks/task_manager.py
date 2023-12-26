# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import copy, re, os
from datetime import datetime, date

# Functions created in different file: minimal code - easy for read
from functions import reg_user#, view_edit_task#,load_tasks, update_task_status, marked_task#, get_tasks_file 

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
print(f"TASK LIST: {task_list}")
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        print(f"\nHello {curr_user.capitalize()}!")
        logged_in = True

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    ds - Display statistics
    e - Exit
    : ''').lower()
    print()

    if menu == 'r':
        while True: # <-- Added loop
            '''Add a new user to the user.txt file'''
            # - Request input of a new username
            new_username = input("New Username: ")

            new_username = reg_user(new_username) # <-- deployed function

            if new_username is False:
                print("\nI'm sorry, this name is taken! Please try agin.")
                break # <-- Break the loop to ask for username again

            # - Request input of a new password
            new_password = input("New Password: ")

            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")

            # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # - If they are the same, add them to the user.txt file,
                print("New user added")
                username_password[new_username] = new_password
                
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))
                    break # <-- Need this

            # - Otherwise you present a relevant message.
            else:
                print("Passwords do no match")

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")

    # open_tasks_file = get_tasks_file()

    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            # Missing
            disp_str += f"Completed: \t {"Yes" if t['completed'] else "No"}\n" 
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            

    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        # curr_user_task = [None]
        curr_user_task_list = []
        for i,t in enumerate(task_list):
            if t['username'] == curr_user:
                disp_str = f"Task {len(curr_user_task_list) + 1}: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t\t {t['username'].capitalize()}\n"
                disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Completed: \t\t {"Yes" if t['completed'] else "No"}\n" # <-- Missing
                disp_str += f"Task Description: \n {t['description']}\n"
                print(f"FIRST PRINT {disp_str}")
                # curr_user_task.append(disp_str)
                curr_user_task_list.append(t)

        num_of_index = [i for i in range(1, len(curr_user_task_list) + 1)]
        # selected_task = 0
        
        # print(curr_user_task)
        # print(f"CURR USER LIST OF TASK {curr_user_task_list}\n\n")
        # print(f"ALL LIST OF TASK {task_list}")
    
        while True:
            specific_task = input('''Select one of the following options below:
    -1 - Return to the main menu
    tc - Mark the task as complete
    et - Edit the task
    : ''').lower()
            selected_task = {}
            if specific_task == "-1":
                break
            elif specific_task == "tc":
                while True:
                    task_num = input(f"""\nTask: {', '.join(map(str, num_of_index))}.\n\nWhich task have you completed? """)
                    print()

                    try:
                        task_num = int(task_num)
                        if task_num < 1 or task_num >= len(num_of_index):
                            print("Invalid task number. Please enter a valid task number.\n")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid task number.\n")
                        break

                    selected_task = curr_user_task_list[task_num - 1]
                    found_task = False  # Flag to track if the condition is met
                    print(f"SELECTED TASK: {selected_task}")
                    # print(f"ORIGINA LIST: {task_list}")

                    with open("tasks.txt", "r+") as task_file:
                        task_list_to_write = []
                        for task in task_file:
                            print(f"OPENED FROM FILE: {task}")
                            if selected_task == task and task["completed"]:
                                print(selected_task)
                                print(f"Task {task_num} is already completed.")
                                found_task = True  # Set the flag to True
                                break
                            elif selected_task == task and not task["completed"]:
                                answer = input(f"Mark task {task_num} as complete? (Y / N): ").lower()
                                if answer == "y":
                                    task['completed'] = True
                                    print(f"\nTask {task_num} marked as complete.")
                                    print(f"MATCHED TASK: {task}")
                                    break
                                elif answer == "n":
                                    print(f"\nTask {task_num} not marked as complete.")
                                    break
                        #     str_attrs = [
                        #         t['username'],
                        #         t['title'],
                        #         t['description'],
                        #         t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        #         t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        #         "Yes" if t['completed'] else "No"
                        #     ]
                        #     task_list_to_write.append(";".join(str_attrs))
                        # task_file.write("\n".join(task_list_to_write))
                    
                    # for task in task_list:
                        

            """

        # Re-arranged index task(s) for each user        
        task_result = view_edit_task(curr_user_task)

        if task_result != False:
            while True:
                specific_task = input('''Select one of the following options below:
                    -1 - Return to the main menu
                    tc - Mark the task as complete
                    et - Edit the task
                    : ''').lower()

                if specific_task == "-1":
                    break
                elif specific_task == "tc":
                    # num_of_index = []
                    # all_tasks = []
                    selected_task = {}

                    num_of_index = [i for i in range(1, len(task_result))]
                    all_tasks = []

                    for i, t in enumerate(task_result):
                        if i == 0:
                            continue  # Skip the header

                    task_num = input(f"\nWhich task: {', '.join(map(str, num_of_index))}? ")

                    try:
                        task_num = int(task_num)
                        if task_num < 1 or task_num >= len(num_of_index):
                            print("Invalid task number. Please enter a valid task number.")
                            # return
                    except ValueError:
                        print("Invalid input. Please enter a valid task number.")
                        # return

                    selected_task = task_list[task_result]

                    if selected_task['completed']:
                        print(f"Task {task_num} is already completed.")
                    else:
                        answer = input(f"Mark task {task_num} as complete? (Y / N): ").lower()
                        if answer == "y":
                            selected_task['completed'] = True
                            print(f"Task {task_num} marked as complete.")
                        elif answer == "n":
                            print(f"Task {task_num} not marked as complete.")
                        else:
                            print("Invalid input. Please enter 'Y' or 'N'.")
                # elif specific_task == et:
                else: 
                    print("\nThat's not an option! Please try again: \n")   
        else:
            while True:
                specific_task = input("Type -1 to return to the main menu: ").lower()
                if specific_task == "-1":
                    break
                else: 
                    print("\nThat's not an option! Please try again: \n") 
                    """
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")