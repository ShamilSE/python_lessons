a = 1
while a < 101:
  if a % 7 == 0 and a % 4 == 0:
    print('fizzbuzz')
  elif a % 4 == 0:
    print('fizz')
  elif a % 7 == 0:
    print('buzz')
  else:
    print(a)
  a += 1
