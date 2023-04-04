import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

style.configure("CustomEntryStyle.TEntry", padding=20) # Criando o estilo
style.configure("CustomEntryStyle.TEntry", )
style.configure("Emergency.CustomEntryStyle.TEntry", padding=20) # Criando o estilo

name = ttk.Label(root, text="Hello, World!") # Aparece o texto
entry = ttk.Entry(root, width=15) # Caixa para digitar
entry["style"] = "CustomEntryStyle.TEntry" # Chamando o estilo
name.pack()
entry.pack()

entry2 = ttk.Entry(root, width=15, style="CustomEntryStyle.TEntry")
entry2.pack()


root.mainloop()