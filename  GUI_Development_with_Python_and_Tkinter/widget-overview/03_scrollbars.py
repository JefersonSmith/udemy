import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = tk.Text(root, height=8)
text.grid(row=0, column=0, sticky="ew")
text.insert("1.0", "Please enter a coment...")

# Criando scrollbar
text_scroll = ttk.Scrollbar(root, orient="vertical", command="text.yview")
text_scroll.grid(row=0, column=1, sticky="ns")
# linkando a barra de scroll ao texto
text["yscrollcommand"] = text_scroll.set

root.mainloop()