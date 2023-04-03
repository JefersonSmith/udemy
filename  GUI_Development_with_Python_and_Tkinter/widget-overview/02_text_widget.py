import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

text = tk.Text(root, height=8)
text.pack() #Caixa de texto com 8 linhas

text.insert("1.0", "Please enter a coment...")
# 1.0 = a posicação do texto, linha 1 caractere 0
text["state"] = "normal" #disabled - liga e desliga a caixa de texto

text_content = text.get("1.0", "end")
print(text_content)

root.mainloop()