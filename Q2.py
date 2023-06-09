# 1から100まで繰り返し、素数の数値を表示するプログラムを作成しましょう。

for i in range(2, 100):
  if i == 2:
    print(i)
  else:
    for n in range(2, i):
      if i % n == 0:
        break
      elif n == i - 1:
        print(i)
      else:
        pass

#ユーザー定義関数使うともっとわかりやすい
#   def is_prime(number):
#     # 引数のnumberが素数ならTrueを返す
#     for j in range(2, number):
#       # print(f'  j={j}')
#       if i % j == 0:
#         return False
#
#     # 割り切れなかったら（素数じゃなかったら）ここに到達する
#     return True
#
# for i in range(2, 101):
#   if is_prime(i):
#     print(i)

# 回答例
# for i in range(2, 101):
#     is_prime = True  # 素数かどうかのフラグ
#     # i = 10
#     # 2~9までで、割ってみて
#     # 割れきれたら素数じゃない
#     # print(f'i={i}')
#     for j in range(2, i):
#         # print(f'  j={j}')
#         if i % j == 0:
#             is_prime = False
#
#     if is_prime:
#         print(i)




