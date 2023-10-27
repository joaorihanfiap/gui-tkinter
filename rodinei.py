from tkinter import *
import random



def muda_imagem():
    nova_imagem = "aula 13/jogo_img/" + escolha.get() + '.png'
    imagem1["file"] = nova_imagem

def comp():
    rando = ["tesoura", "pedra", "papel"]
    rand = random.choice(rando)
    nova_img = "aula 13/jogo_img/" + rand + '.png'
    imagem2["file"] = nova_img

    if escolha.get() == "pedra" and rand == "pedra":
        rotulo_texto3['text'] = 'Empate'
    
    if escolha.get() == "papel" and rand == "papel":
        rotulo_texto3['text'] = 'Empate'
    
    if escolha.get() == "tesoura" and rand == "tesoura":
        rotulo_texto3['text'] = 'Empate'
    
    if escolha.get() == "pedra" and rand == "tesoura":
        rotulo_texto3['text'] = 'Venceu!'
        rotulo_texto3['fg'] = 'green'    
    if escolha.get() == "tesoura" and rand == "papel":
        rotulo_texto3['text'] = 'Venceu!'
        rotulo_texto3['fg'] = 'green'   
    if escolha.get() == "papel" and rand == "pedra":
        rotulo_texto3['text'] = 'Venceu!'
        rotulo_texto3['fg'] = 'green'  
    if escolha.get() == "pedra" and rand == "papel":
        rotulo_texto3['text'] = 'Perdeu'
        rotulo_texto3['fg'] = 'red'          
    if escolha.get() == "papel" and rand == "tesoura":
        rotulo_texto3['text'] = 'Perdeu'
        rotulo_texto3['fg'] = 'red'         
    if escolha.get() == "tesoura" and rand == "pedra":
        rotulo_texto3['text'] = 'Perdeu'
        rotulo_texto3['fg'] = 'red'

window = Tk()
window.title("ai novinha")
window.geometry("1000x600")
window.configure(bg="goldenrod")

fonte = ("Arial", "13")
escolha = StringVar()
escolha.set("chaplin")
container1 = Frame(window,padx=10, bg="goldenrod")
container2 = Frame(window,padx=10, bg="goldenrod")
container3 = Frame(window,padx=10, bg="goldenrod")
container4 = Frame(window,padx=10, bg="goldenrod")
container1.pack(side=LEFT)
container2.pack(side=LEFT)
container3.pack(side=LEFT)


texto = ["Tesoura", "Pedra", "Papel"]
valor = ["tesoura", "pedra", "papel"]


for i in range(0, 3, 1):
    Radiobutton(container1, text=texto[i], indicatoron=False, value=valor[i], variable=escolha, width=15, anchor="w", padx=10, pady=5, bg="goldenrod", font=fonte, command=muda_imagem).pack()


imagem1 = PhotoImage(file="aula 13/jogo_img/vazio.png")

rotulo_texto1 = Label(container2,text="Sua Jogada", font=fonte, padx=10)
rotulo_texto2 = Label(container3,text="Maquina", font=fonte, padx=10)
rotulo_texto3 = Label(container3,text="Resultado", font=fonte, padx=10)

rotulo_texto1.pack(side=TOP)
rotulo_texto2.pack(side=TOP)
rotulo_texto3.pack(side=BOTTOM)

rotulo = Label(container2, image=imagem1)
imagem2 = PhotoImage(file="aula 13/jogo_img/vazio.png")
rotulo2 = Label(container3, image=imagem2)

botao = Button(container2, text="Jogar", font=fonte, command=comp)


botao.pack(side=BOTTOM)
rotulo.pack(side=LEFT)
rotulo2.pack(side=RIGHT)


window.mainloop()