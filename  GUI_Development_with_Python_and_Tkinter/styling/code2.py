import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, World!")
entry = ttk.Entry(root, width=15)
name.pack()

style.configure("TLabel", font=("Segor UI", 20))

#print(name.winfo_class()) # Checa a classe

root.mainloop()