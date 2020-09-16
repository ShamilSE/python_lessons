from tkinter import *

def handler1(event):
    print('Hello world!')

# инициализация
root = Tk()
hello_label = Label(root, text="Hello world", font="Times 40")
hello_label.pack()

# привязка обработчиков
hello_label.bind("<Button-1>", handler1)

# главный цикл
root.mainLoop()
