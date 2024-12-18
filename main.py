#Задание 1

from tkinter import *
import random

def random_number():
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