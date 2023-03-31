import tkinter as tk

root = tk.Tk()
root.geometry("600x400") #Tamanho inicial da janela

#o código abaixo cria uma label com a cor de fundo verde e texto branco
rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True) # define o tamanho e adiciona na janela com o comando pack

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(side="top", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_3 = tk.Label(root, text="Rectangle 3", bg="black", fg="white")
rectangle_3.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

root.mainloop()



