#Задание 1, 2

from tkinter import *
from tkinter import ttk
import random

def random_number():
    min_num = int(min_combobox.get())
    max_num = int(max_combobox.get())

    if min_num < max_num:
        number = random.randint(min_num, max_num)
        result.config(text=str(number))
    else:
        result.config(text="Error")

root = Tk()
root.title("Random num")
root.geometry("300x300")

button = Button(root, text="Generate", command=random_number)
button.pack(pady=20)

label = Label(root, text="")
label.pack()


root.mainloop()