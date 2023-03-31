import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk()

user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ") #cria a label nome
name_label.pack(side="left", padx=(0, 10)) #padx da um espaço ao lado do nome
name_entry = ttk.Entry(root, width=15, textvariable=user_name) #espaço para o usuario digitar o nome
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root, text="Greet", command=greet) #cria um botão que chama a função greet
greet_button.pack(side="left", fill="x", expand=True) #side coloca o botão na esquerda, fill preenche
# a posição Y, X ou Both e expand, faz o icone expandir quando aumentamos a janela

quit_button = ttk.Button(root, text="Quit", command=root.destroy)#cria o botão quit que destrói a jenela e encerra.
quit_button.pack(side="left", fill="x", expand=True)

root.mainloop()

