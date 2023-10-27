from tkinter import * 

def jogar():
    import random
    nova_imagem = "./jogo_img/" + escolha.get() +'.png'
    imagem_jogador['file'] = nova_imagem

    imagem_aleatoria = random.choice(valor)

    nova_imagem = "./jogo_img/" + imagem_aleatoria +'.png'
    imagem_bot['file'] = nova_imagem


window = Tk()

window.geometry("600x400+300+300")
window.configure(bg="moccasin")
fonte = ("Arial", "16")

escolha = StringVar()
escolha.set("vazio")

container_escolhas = Frame(window, padx=10)
container_escolhas.pack(side=LEFT)

texto= ["Pedra", "Papel", "Tesoura"]
valor = ["pedra", "papel", "tesoura"]

for i in range(3):
    Radiobutton(container_escolhas, text=texto[i], indicatoron=False, value=valor[i], variable=escolha, width=15, anchor="center", padx=10, pady=5, font=fonte, bg="moccasin").pack()
    
imagem_jogador = PhotoImage(file="./jogo_img/tesoura.png")
imagem_bot = PhotoImage(file="./jogo_img/tesoura.png")

container_imagem_jogador = Frame(window, padx=10, bg="moccasin")
container_imagem_jogador.pack(side=LEFT)

rotulo_imagem_jogador = Label(container_imagem_jogador, image=imagem_jogador)
rotulo_imagem_jogador.pack(side=LEFT)

container_imagem_bot = Frame(window, padx=10, bg="moccasin")
container_imagem_bot.pack(side=LEFT)

rotulo_imagem_bot = Label(container_imagem_bot, image=imagem_bot)
rotulo_imagem_bot.pack(side=LEFT)

botao = Button(container_imagem_jogador, text="Jogar", padx=10, pady=5, bg="purple", fg="white")
botao["command"] = jogar
botao.pack()

window.mainloop()