import tkinter as tk


# CELL_SIZE = 100
# BOARD_SIZE = 4 * CELL_SIZE
# BOARD_SIZE = 500 * 707

WIDTH = 500
HEIGHT = 707

root = tk.Tk()
root.title("Tic-Tac-Toe vs AI!")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

cover_img = tk.PhotoImage(file="cover.png")
canvas.create_image(0, 0, anchor="nw", image=cover_img)

root.mainloop()


root.mainloop()
