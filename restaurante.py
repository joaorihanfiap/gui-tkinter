from tkinter.ttk import *
from tkinter import *




def terminar_pedido():
    precos = {
        "Burger" : 34.90,
        "Noodles" : 44.50,
        "Pizza" : 49.00, 

        "Fritas" : 14.90,
        "Nuggets" : 9.50,
        "Milho" : 12.00,

        "Suco" : 14.90,
        "Shake" : 19.90
    }

    mudar_lanche = "./cardapio/" + combo_lanche.get() +'.png'
    imagem_lanche['file'] = mudar_lanche
    mudar_acomp = "./cardapio/" + combo_acomp.get() +'.png'
    imagem_acomp['file'] = mudar_acomp
    mudar_bebida = "./cardapio/" + combo_bebida.get() +'.png'
    imagem_bebida['file'] = mudar_bebida

    soma = precos[combo_lanche.get()] + precos[combo_acomp.get()] + precos[combo_bebida.get()]
    texto_total2['text'] = soma




fonte = ('Impact', '14')
window = Tk()
window.title('ttkinter')
window.geometry('550x400+375+200')

#Lanche
container_lanche = Frame(window, pady= 5, padx = 10)
container_lanche.pack()

texto_lanche = Label(container_lanche, text='Lanche:', pady=3, font=fonte)
texto_lanche.pack(side=LEFT)

combo_lanche = Combobox(container_lanche)
combo_lanche['values'] = ("Burger", "Noodles", "Pizza")
combo_lanche['state']= 'readonly'
combo_lanche.pack(side=RIGHT)
combo_lanche.current(0)

#Acompanhamento

container_acomp = Frame(window, pady= 5, padx = 10)
container_acomp.pack()

texto_acomp = Label(container_acomp, text='Porção:', pady=3, font=fonte)
texto_acomp.pack(side=LEFT)

combo_acomp = Combobox(container_acomp)
combo_acomp['values'] = ("Fritas", "Nuggets", "Milho")
combo_acomp['state']= 'readonly'
combo_acomp.pack(side=RIGHT)
combo_acomp.current(0)

#bebida

container_bebida = Frame(window, pady= 5, padx = 10)
container_bebida.pack()

texto_bebida = Label(container_bebida, text='Bebida:', pady=3, font=fonte)
texto_bebida.pack(side=LEFT)

combo_bebida = Combobox(container_bebida)
combo_bebida['values'] = ("Suco", "Shake")
combo_bebida['state']= 'readonly'
combo_bebida.pack(side=RIGHT)
combo_bebida.current(0)

#Imagem

container_imagens = Frame(window, pady=10, padx=50)
container_imagens.pack()

imagem_lanche = PhotoImage(file='./cardapio/escolha.png')
imagem_acomp = PhotoImage(file='./cardapio/escolha.png')
imagem_bebida = PhotoImage(file='./cardapio/escolha.png')

rotulo1 = Label(container_imagens, image=imagem_lanche)
rotulo2 = Label(container_imagens, image=imagem_acomp)
rotulo3 = Label(container_imagens, image=imagem_bebida)
rotulo1.pack(side=LEFT)
rotulo2.pack(side=LEFT)
rotulo3.pack(side=LEFT)

container_botao = Frame(window, pady=5, padx=10)
container_botao.pack()
botao = Button(container_botao, text="Fazer Pedido", padx=15, pady=5, bg="purple", fg="white")
botao["font"] = fonte
botao['command'] = terminar_pedido
botao.pack()

container_total = Frame(window, pady=5, padx=10)
container_total.pack()
texto_total = Label(container_total)
texto_total["text"] = "Total: R$"
texto_total["font"] = fonte
texto_total.pack(side=LEFT)

texto_total2 = Label(container_total)
texto_total2["font"] = fonte
texto_total2.pack(side=LEFT)


window.mainloop()




