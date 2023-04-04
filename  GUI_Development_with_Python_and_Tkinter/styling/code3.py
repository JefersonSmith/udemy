import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, World!")
entry = ttk.Entry(root, width=15)
name.pack()

print(style.layout("TLabel"))

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

style.theme_use("clam")

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

style.configure("TLabel", bordercolor="#f00") #adiciona a cor vermelha na borda
style.configure("TLabel", borderwidth=20) #tamanho da borda
style.configure("TLabel", relief="solid") #faz a borda aparacer

root.mainloop()