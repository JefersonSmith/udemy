import tkinter as tk
import tkinter.font as font # importando novas fontes
from tkinter import ttk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Distance converter") # Titulo do aplicativo

#Trocando a fonte
font.nametofont("TkDefaultFont").configure(size=15)

metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")

def calculate_feet(*args): # comando para calcular a conversao
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass

root.columnconfigure(0, weight=1) #mantem centralizado quando expandimos a janela

main = ttk.Frame(root, padding=(30, 15))
main.grid()

metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)#command adiciona o def criado acima

metres_label.grid(column=0, row=0, sticky="w", padx=15, pady=15) #sticky vai alinhar o texto
metres_input.grid(column=1, row=0, sticky="EW", padx=15, pady=15)
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="w", padx=15, pady=15)
feet_display.grid(column=1, row=1, sticky="EW", padx=15, pady=15)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5) # Estica o botao


#criando atalhosno teclado
root.bind("<Return>", calculate_feet) # apertar ENTER (<Return>) faz calcular
root.bind("<KP_Enter>", calculate_feet) # apertar ENTER numerico (<KP_Enter>) faz calcular


root.mainloop()