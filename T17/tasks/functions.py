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

  task_num = input(
      f"\nTask: {', '.join(map(str, num_of_index))}\n\nSelect task number: ")
  print()

  try:
    task_num = int(task_num)
    if task_num < 1 or task_num > len(num_of_index):
      print("Invalid task number. Please enter a valid task number.")
      return False
    else:
      return int(task_num)
  except ValueError:
    print("Invalid input. Please enter a valid task number.\n")
    return False


def selecting_username(names):

  split_name_str = [n.replace(";", " ") for n in names]
  username_and_pass = [n.split(";") for n in names]
  username_only = [n[0] for n in username_and_pass]

  # print(f"1: {username_and_pass}")
  # print(f"2: {username_only[1]}")

  all_user_names = {}
  for i, n in enumerate(split_name_str):
    all_user_names[i + 1] = n

  index_and_name = {}
  # Print dictionary items horizontally
  all_user_names = ", ".join(f"{key}: {value}"
                             for key, value in all_user_names.items())
  selected_user_index = int(
      input(
          f"Users: {all_user_names.replace(':', '.')}\n\nRe-assign to which user? Select the index number: "
      ))
  selected_name = {"name": username_only[selected_user_index - 1]}
  # print(index_and_name)

  return selected_name

  # try:
  #     username = int(username)
  #     if username < 1 or username > len(names):
  #         print("Invalid name index. Please enter a valid name index.")
  #         return 0
  #     else:
  #         return username
  # except ValueError:
  #     print("Invalid input. Please enter a valid nane index.")
  #     return 0
