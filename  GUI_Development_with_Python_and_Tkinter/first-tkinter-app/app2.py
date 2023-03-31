import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello, World!")

root = tk.Tk()

greet_button = ttk.Button(root, text="Greet", command=greet) #cria um botão que chama a função greet
greet_button.pack(side="left", fill="x", expand=True) #side coloca o botão na esquerda, fill preenche
# a posição Y, X ou Both e expand, faz o icone expandir quando aumentamos a janela

quit_button = ttk.Button(root, text="Quit", command=root.destroy)#cria o botão quit que destrói a jenela e encerra.
quit_button.pack(side="left")

root.mainloop()

