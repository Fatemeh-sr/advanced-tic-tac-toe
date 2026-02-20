import tkinter as tk

from tkinter import PhotoImage
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # وقتی exe شده
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("Tic-Tac-Toe vs AI!")

cover_img = PhotoImage(file=resource_path("images/cover.png"))
x_img = PhotoImage(file=resource_path("images/x.png"))
o_img = PhotoImage(file=resource_path("images/o.png"))

WIDTH = 500
HEIGHT = 707
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_image(0, 0, anchor="nw", image=cover_img)
canvas.cover_img = cover_img

root.mainloop()
