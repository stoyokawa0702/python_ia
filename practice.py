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


