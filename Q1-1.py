# 演習問題1.
# 下に書きかけのプログラムがあります。
# 辞書のkeyとvalueをそれぞれinput関数で受けとり、user_dict辞書をprint関数で表示すると、
# {入力したkey: 入力したvalue}
# と表示されるプログラムを作成しましょう。
# (data_dict辞書にkey:valueを追加するという処理を書く必要があります)
data_dict = {}

key = input('keyを入力してください > ')  # 辞書のkeyを入力してもらう
value = input('valueを入力してください > ')  # 辞書のvalueを入力してもらう

data_dict = {key:value}
# こっちでもいい
# data_dict[key] = value

# この辺に何かを書く

print(data_dict)