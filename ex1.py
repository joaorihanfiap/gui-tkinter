from tkinter import *


window = Tk()


window.title("Título")
window.geometry("400x200+450+200")
window.configure(background="aqua")
rotulo = Label(window)
rotulo.configure(background="aqua")
rotulo["text"] = "HAHAHAHAHHAHAH"
rotulo["font"] = ("Arial", "20", "bold")
rotulo["fg"] = "red"
rotulo["pady"] = "5"
rotulo["padx"] = "10"
rotulo["width"] = "20"
rotulo["anchor"] = "w"
rotulo.pack()

window.mainloop()