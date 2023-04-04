import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

style.theme_use(("clam")) # mudando o tema

style.map("CustomButton.TButton",
          foreground=[("pressed", "red"), ("active", "white")], #pressed - apertar o botao / #active - passar o mouse
          background=[("pressed", "disabled", "black"), ("active", "black")], # mudando a cor de fundo do botao
          font=[("pressed", ("TkDefaultFont", 15))] # Aumenta a fonte quando pressionado o botao
)

name = ttk.Label(root, text="Hello, World!") # Aparece o texto
entry = ttk.Entry(root, width=15) # Caixa para digitar
button = ttk.Button(root, text="Press me.", style="CustomButton.TButton") # cria o botao com texto
name.pack()
entry.pack()
button.pack()

root.mainloop()