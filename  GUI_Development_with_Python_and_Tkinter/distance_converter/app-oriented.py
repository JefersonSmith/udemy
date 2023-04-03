import tkinter as tk
import tkinter.font as font # importando novas fontes
from tkinter import ttk
from PIL import Image, ImageTk

class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")

        frame = MetresToFeet(self, padding=(60, 30))
        frame.grid()

        self.bind("<Return>", frame.calculate_feet)
        self.bind("<KP_Enter>", frame.calculate_feet)

class MetresToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        metres_label = ttk.Label(self, text="Metres:")
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Segoe UI", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate_feet)

        metres_label.grid(column=0, row=0, sticky="w")  # sticky vai alinhar o texto
        metres_input.grid(column=1, row=0, sticky="EW")
        metres_input.focus()

        feet_label.grid(column=0, row=1, sticky="w")
        feet_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)


    def calculate_feet(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass

root = DistanceConverter()

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1) #mantem centralizado quando expandimos a janela

root.mainloop()