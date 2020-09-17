# в python можно пользоваться глобальными переменными в функциях
# LEGB - local en... (unlocal) global buildins
x = 10

def printer():
  global x
  x = x + 10
  print(x)

printer()