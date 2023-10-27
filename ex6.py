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

radio_chaplin = Radiobutton(container1, text="Charles Chaplin", value="chaplin", variable=escolha, width=15, anchor="w", padx=10, pady=5, font=fonte, command=mudar_imagem)

radio_arlequina = Radiobutton(container1, text="Harley Queen", value="arlequina", variable=escolha, width=15, anchor="w", padx=10, pady=5, font=fonte, command=mudar_imagem)

radio_ninja = Radiobutton(container1, text="Ninja do Deserto", value="ninja", variable=escolha, width=15, anchor="w", padx=10, pady=5, font=fonte, command=mudar_imagem)

radio_zorro = Radiobutton(container1, text="Copo do Zorro", value="zorro", variable=escolha, width=15, anchor="w", padx=10, pady=5, font=fonte, command=mudar_imagem)


radio_chaplin.pack()
radio_arlequina.pack()
radio_ninja.pack()
radio_zorro.pack()

imagem = PhotoImage(file="./imagens/chaplin.png")

rotulo_imagem = Label(container2, image=imagem)
rotulo_imagem.pack(side=RIGHT)



window.mainloop()