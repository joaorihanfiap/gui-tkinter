from tkinter import *

def mudar_imagem():
    nova_imagem = "./imagens/" + escolha.get() +'.png'
    imagem['file'] = nova_imagem


window = Tk()
window.title("Cria")
window.geometry("450x400+250+250")
fonte = ("Arial", "12")

escolha = StringVar()
escolha.set("chaplin")

container1 = Frame(window, padx=10)
container2 = Frame(window, padx=10)
container1.pack(side=LEFT)
container2.pack(side=RIGHT)

texto= ["Charles Chaplin", "Harley Queen", "Ninja do Deserto", "Copo do Zorro"]
valor = ["chaplin", "arlequina", "ninja", "zorro"]

for i in range(4):
    Radiobutton(container1, text=texto[i], indicatoron=False, value=valor[i], variable=escolha, width=15, anchor="w", padx=10, pady=5, font=fonte, command=mudar_imagem).pack()
    

imagem = PhotoImage(file="./imagens/chaplin.png")

rotulo_imagem = Label(container2, image=imagem)
rotulo_imagem.pack(side=RIGHT)



window.mainloop()