import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk()
root.title("Greeter") # Titulo do programa

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0)) # left - top - right - bottom
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name: ") #cria a label nome
name_label.pack(side="left", padx=(0, 10)) #padx da um espaço ao lado do nome
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name) #espaço para o usuario digitar o nome
name_entry.pack(side="left")
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10)) # left and right = 20 top and bottom = 10
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet", command=greet) #cria um botão que chama a função greet
greet_button.pack(side="left", fill="x", expand=True) #side coloca o botão na esquerda, fill preenche
# a posição Y, X ou Both e expand, faz o icone expandir quando aumentamos a janela

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)#cria o botão quit que destrói a jenela e encerra.
quit_button.pack(side="left", fill="x", expand=True)

root.mainloop()

