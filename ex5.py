from tkinter import *

def verificar_box():
    mensagem = "Seus pertences: "
    if tv.get():
        mensagem += "\n" + check_tv["text"]
    if pc.get():
        mensagem += "\n" + check_pc["text"]
    if vg.get():
        mensagem += "\n" + check_vg["text"]
    if bk.get():
        mensagem += "\n" + check_bk["text"]
    rotulo1["text"] = mensagem

fonte = ("Arial", "12")
window = Tk()

window.title("Checkbox")
window.geometry("400x200+250+250")

tv = BooleanVar()
pc = BooleanVar()
vg = BooleanVar()
bk = BooleanVar()


container1 = Frame(window)
container2 = Frame(window)

container1.pack(side=LEFT)
container2.pack(side=TOP)

check_tv = Checkbutton(container1, text="Televisão", font=fonte, variable=tv, width=15, padx=10, pady=5, anchor="w", command=verificar_box)

check_pc = Checkbutton(container1, text="Computador", font=fonte, variable=pc, width=15, padx=10, pady=5, anchor="w", command=verificar_box)

check_vg = Checkbutton(container1, text="Videogame", font=fonte, variable=vg, width=15, padx=10, pady=5, anchor="w", command=verificar_box)

check_bk = Checkbutton(container1, text="Bicicleta", font=fonte, variable=bk, width=15, padx=10, pady=5, anchor="w", command=verificar_box)

check_tv.grid(row=0, column=0)
check_pc.grid(row=1, column=0)
check_vg.grid(row=2, column=0)
check_bk.grid(row=3, column=0)

rotulo1 = Label(container2, text="Seus pertences:", font=("Arial", "16", "bold"))
rotulo1.grid(row=0, column=1)


window.mainloop()