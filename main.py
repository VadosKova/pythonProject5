#Задание 1, 2, 3, 4
from tkinter import *
from tkinter import ttk, messagebox
import random

def random_number():
    min_num = int(min_combobox.get())
    max_num = int(max_combobox.get())

    if min_num < max_num:
        black_list = []
        for i in range(exception_listbox.size()):
            black_list.append(int(exception_listbox.get(i)))

        valid_numbers = []
        for num in range(min_num, max_num + 1):
            if num not in black_list:
                valid_numbers.append(num)

        if valid_numbers:
            number = random.choice(valid_numbers)
            result.config(text=str(number))
        else:
            messagebox.showinfo('Error', 'No valid numbers')
    else:
        messagebox.showinfo ('Error', 'From > To')

def add_exception():
    exception = exception_entry.get()
    if exception.isdigit():
        exception_listbox.insert(END, exception)
        exception_entry.delete(0, END)

root = Tk()
root.title("Random num")
root.geometry("300x450")

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

exception_label = Label(root, text="Исключения:")
exception_label.pack(pady=10)

exception_entry = Entry(root)
exception_entry.pack(pady=5)

add_btn = Button(root, text="Add", command=add_exception)
add_btn.pack(pady=5)

exception_listbox = Listbox(root)
exception_listbox.pack(pady=10)


root.mainloop()