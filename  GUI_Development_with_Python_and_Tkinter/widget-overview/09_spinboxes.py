import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

initial_value = tk.StringVar(value=20)
# spin_box = tk.Spinbox(
#     root,
#     from_=0,
#     to=30,
#     textvariable=initial_value,
#     wrap=False
# ) # aqui temos uma lista de 0 a 30

spin_box = tk.Spinbox(
    root,
    values=(5, 10, 15, 20, 25, 30),
    textvariable=initial_value,
    wrap=False
)

spin_box.pack()

print(spin_box.get())

root.mainloop()