# 演習1
# 組み込み関数inoutを使い、名前を入力してEnterを押すと
# こんにちは、{入力した名前}
# と表示されるプログラムを作ってみる

user_input = input()

print('こんにちは、' + user_input)

# こっちでも可
# result = 'こんにちは、' + user_input
# print(result)


# もうちょい古い書き方。formatで、変数を埋め込める
# 'こんにちは{}'.format(user_input_name)
