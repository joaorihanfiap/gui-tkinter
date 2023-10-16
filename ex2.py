from tkinter import *


window = Tk()


window.title("Título")
window.geometry("400x200+450+200")
window.configure(background="aqua")
rotulo = Label(window)
rotulo.configure(background="aqua")
rotulo["text"] = "Hello World"
rotulo["font"] = ("Impact", "20", "bold")
botao = Button(window, text="Click Me!", padx=10, pady=10)
botao["font"] = ("Times New Roman", 16, "bold")
botao["fg"] = "purple"
botao["bg"] = "yellow"
botao["command"] = window.destroy
rotulo.pack()
botao.pack()



window.mainloop()