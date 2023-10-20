from tkinter.ttk import *
from tkinter import *

def muda_imagem():
    nova_imagem = "./imagens/" + combo.get() +'.png'
    imagem['file'] = nova_imagem

fonte = ('Impact', '14')
window = Tk()
window.title('ttkinter')
window.geometry('400x300+500+250')

rotulo1 = Label(window, text='Escolha seu avatar', pady=20, font=fonte)
rotulo1.pack()

container2 = Frame(window, pady=20, padx=10)
container2.pack()
combo = Combobox(container2)
combo['values'] = ('arlequina', 'chaplin', 'gueixa', 'ninja', 'zorro')
combo['state']= 'readonly'
combo.current(0)
combo.pack(side=LEFT)
imagem = PhotoImage(file='./imagens/arlequina.png')
rotulo2 = Label(container2, image=imagem)
rotulo2.pack(side=RIGHT)
botao = Button(window, text='muda imagem', pady=5, padx=10, font=fonte)
botao['command'] = muda_imagem
botao.pack()




window.mainloop()