user_file_text = """

hoge
fuga
taro
ziro
saburo

"""

user_name_list = user_file_text.split()
# user_name_list.sort()
user_name_sort = sorted(user_name_list)
# print(user_name_sort)
user_name_string = '\n'.join(user_name_sort)
print(user_name_string)

# 答えはこっち
# user_name_list = user_file_text.split()
# user_name_list.sort()
# # user_name_string = ' '.join(user_name_list)
# user_name_string = '\n'.join(user_name_list)
# print(user_name_string)