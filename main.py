#Задание 1

from tkinter import *
import random

def random_number():
    number = random.randint(1, 100)
    label.config(text=str(number))