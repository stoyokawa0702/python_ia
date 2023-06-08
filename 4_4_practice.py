# 演習問題2
# 組み込みinput()を使って、「2023」と入力してエンターを押すと、
# 「今は2023年です。来年は2024年です」と表示されるプログラムを作りましょう。

user_input = input()
year = int(user_input) + 1
print('今は' + str(user_input) + '年です。来年は' + str(year) + '年です。')

# これでもかけちゃう
# print(f'今は{user_input}年です。来年は{year}です。')