class Goat:
  # параметры класса - атрибуты
  age = 0
  name = ""
  weight = 0.0
  # self обязателен, ссылка на объект, для которого вызван этот метод
  def show(self):
    # функция в классе - метод
    print(self.name)
    print(self.age)

# Объект - экземпляр класса
a = Goat()
print(type(a))
a.name = "Зорька"
a.age = 2
a.age += 1

b = Goat()
b.name = "Нотка"
b.age = 5

a.show()
b.show()

# --------------------------------------
class Student():
  # конструктор
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(name, '+')

# передача параметров конструктору
Vasya = Student("Вася", 17)