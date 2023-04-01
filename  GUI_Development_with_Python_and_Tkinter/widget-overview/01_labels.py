import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

image = Image.open("logo.png").resize((64, 64))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, text="Python is the best", image=photo, padding=5, compound="right") # Texto ao lado da imagem
label.pack()


root.mainloop()