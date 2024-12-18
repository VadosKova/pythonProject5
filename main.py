#Задание 1, 2

from tkinter import *
from tkinter import ttk
import random

def random_number():
    min_num = int(min_combobox.get())
    max_num = int(max_combobox.get())
    number = random.randint(1, 100)
    label.config(text=str(number))

root = Tk()
root.title("Random num")
root.geometry("300x300")

button = Button(root, text="Generate", command=random_number)
button.pack(pady=20)

label = Label(root, text="")
label.pack()


root.mainloop()