from tkinter import *

def somar():
    soma = int(caixa_texto1.get()) + int(caixa_texto2.get())
    somatotal["text"] = soma
    return soma

window = Tk()
window.title("Soma")
window.geometry("400x250+450+200")

titulo_pag = Label(window, text="Digite dois números abaixo:", font="Impact 16 bold", padx=10, pady= 10)
titulo_pag.pack()

container = Frame(window, padx=10, pady=15)
container.pack()

rotulo1 = Label(container, text="Nº 1", font="Arial 16", pady=5, padx=5)
rotulo1.pack(side=LEFT)

caixa_texto1 = Entry(container, font=("Times New Roman", "16"), width=5)
caixa_texto1.pack(side=LEFT)

caixa_texto2 = Entry(container, font=("Times New Roman", "16"), width=5)
caixa_texto2.pack(side=RIGHT)


rotulo2 = Label(container, text="Nº 2", font="Arial 16", pady=5, padx=5)
rotulo2.pack(side=RIGHT)

container2 = Frame(window, pady=10, padx=15)
container2.pack()

container3 = Frame(window, pady=10, padx=15)
container3.pack()



botao = Button(container3, text="Somar", padx=10, pady=5, bg="purple", fg="white")
botao["font"] = ("Courrier New", "16")
botao["command"] = somar
botao.pack()

rotulo3 = Label(container2, font="Arial 16", padx=5, pady=10)
rotulo3["text"] = "Resultado: "
rotulo3.pack(side=LEFT)

somatotal = Label(container2, font="Arial 16", padx=5, pady=10)
somatotal.pack(side=LEFT)

caixa_texto1.focus()

window.mainloop()