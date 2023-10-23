from tkinter import *

def verificar_box():
    mensagem = "Seus pertences: "
    if ballistamon.get():
        imagem_digimon['file'] = './digimon/ballistamon.png'
    if dorulumon.get():
        imagem_digimon['file'] = './digimon/dorulumon.png'
    if shoutmon.get():
        imagem_digimon['file'] = './digimon/shoutmon.png'
    if shoutmon.get() and ballistamon.get():
        imagem_digimon['file'] = './digimon/shoutmonX2.png'
    if shoutmon.get() and dorulumon.get():
        imagem_digimon['file'] = './digimon/shoutmonX3.png'
    if dorulumon.get() and ballistamon.get():
        imagem_digimon['file'] = './digimon/shoutmonX4.png'        
    if dorulumon.get() and ballistamon.get() and shoutmon.get():
        imagem_digimon['file'] = './digimon/shoutmonX5.png'       
    if not dorulumon.get() and not ballistamon.get() and not shoutmon.get():     
        imagem_digimon['file'] = './digimon/desconhecido.png'       


fonte = ("Arial", "12")
window = Tk()

window.title("Checkbox")
window.geometry("550x350+250+250")

ballistamon = BooleanVar()
dorulumon = BooleanVar()
shoutmon = BooleanVar()


container1 = Frame(window)
container2 = Frame(window)

container1.pack(side=LEFT)
container2.pack(side=TOP)

rotulo2 = Label(container2, text="Selecine seu digimon!", anchor="e", font=('Impact', '16', 'bold'))
rotulo2.pack(side=LEFT)
check_ballistamon = Checkbutton(container1, text="Ballistamon", font=fonte, variable=ballistamon, width=15, padx=10, pady=5, anchor="w", command=verificar_box)

check_dorulumon = Checkbutton(container1, text="Dorulumon", font=fonte, variable=dorulumon, width=15, padx=10, pady=5, anchor="w", command=verificar_box)

check_shoutmon = Checkbutton(container1, text="Shoutmon", font=fonte, variable=shoutmon, width=15, padx=10, pady=5, anchor="w", command=verificar_box)


check_ballistamon.grid(row=0, column=0)
check_dorulumon.grid(row=1, column=0)
check_shoutmon.grid(row=2, column=0)

container_imagens = Frame(window, pady=10, padx=50)
container_imagens.pack()

imagem_digimon = PhotoImage(file='./digimon/desconhecido.png')


rotulo1 = Label(container_imagens, image=imagem_digimon)
rotulo1.pack(side=RIGHT)

window.mainloop()