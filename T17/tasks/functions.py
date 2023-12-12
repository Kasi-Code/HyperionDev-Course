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


def arrange_task_index (i):
    index = 0
    index_list = []
    index_dic = {}
    for j in len(i):
        index_list.append(j)
        index_dic = [(j, index_list)]
        index_dic = dict(index_dic)
        index += 1
    
        return index_dic
    print(index_dic)