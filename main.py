#Задание 1, 2, 3

from tkinter import *
from tkinter import ttk, messagebox
import random

def random_number():
    min_num = int(min_combobox.get())
    max_num = int(max_combobox.get())

    if min_num < max_num:
        number = random.randint(min_num, max_num)
        result.config(text=str(number))
    else:
        messagebox.showinfo ('Error', 'From > To')

root = Tk()
root.title("Random num")
root.geometry("350x350")

label_diapason = Label(root, text="Диапазон:")
label_diapason.pack(pady=10)

min_label = Label(root, text="От:")
min_label.pack(pady=5)

min_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 101)])
min_combobox.set("1")
min_combobox.pack(pady=5)

max_label = Label(root, text="До:")
max_label.pack(pady=5)

max_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 101)])
max_combobox.set("100")
max_combobox.pack(pady=5)

button = Button(root, text="Generate", command=random_number)
button.pack(pady=20)

result = Label(root, text="")
result.pack()


root.mainloop()