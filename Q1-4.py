user_file_text = """

hoge
fuga
taro
ziro
saburo

"""

user_name_list = user_file_text.split()
user_name_list.sort()
# print(user_name_list)
user_name_string = '\n'.join(user_name_list)
print(user_name_string)