import tkinter as tk
import tkinter.font as font # importando novas fontes
from tkinter import ttk
from PIL import Image, ImageTk

class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        feet_to_metres = FeetToMetres(container, self)
        feet_to_metres.grid(row=0, column=0, sticky="NSEW")

        metres_to_feet = MetresToFeet(container, self)
        metres_to_feet.grid(row=0, column=0, sticky="NSEW")

        self.frames[FeetToMetres] = feet_to_metres
        self.frames[MetresToFeet] = metres_to_feet

        for FrameClass in (MetresToFeet, FeetToMetres):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        metres_label = ttk.Label(self, text="Metres:")
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Segoe UI", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Swtich to feet conversion",
            command=lambda: controller.show_frame(FeetToMetres)
        )

        metres_label.grid(column=0, row=0, sticky="w")  # sticky vai alinhar o texto
        metres_input.grid(column=1, row=0, sticky="EW")
        metres_input.focus()

        feet_label.grid(column=0, row=1, sticky="w")
        feet_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)


    def calculate(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass

class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Segoe UI", 15))
        metres_label = ttk.Label(self, text="Metres:")
        metres_display = ttk.Label(self, textvariable=self.metres_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Swtich to feet conversion",
            command=lambda: controller.show_frame(MetresToFeet)
        )


        feet_label.grid(column=0, row=0, sticky="w")
        feet_input.grid(column=1, row=0, sticky="EW")
        feet_input.focus()

        metres_label.grid(column=0, row=1, sticky="w")  # sticky vai alinhar o texto
        metres_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")


        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)



    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            metres = feet / 3.28084
            self.metres_value.set(f"{metres:.3f}")
        except ValueError:
            pass

root = DistanceConverter()

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1) #mantem centralizado quando expandimos a janela

root.mainloop()