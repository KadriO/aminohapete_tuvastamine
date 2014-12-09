#hetkel veel raskusastme osa poolik, aga lõpetan selle siis, kui muu programmi osa saan tööle

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#from tkinter import messagebox

#Raskuksastmed, kõige raskema puhul vihjeid ei pane, kergemal tasemel on vihjeks/
#aminohappe kolmetäheline lühend, keskmisel ühetäheline

sonastik_lihtsam ={"alaniin": "Ala", "arginiin": "Arg", "asparagiin": "Asn"
    , "asparagiinhape": "Asp", "Glutamiin": "Gln", "Glutamiinhape": "Glu",
    "glütsiin": "Gly", "histidiin": "His", "isoleutsiin": "Ile", "leutsiin": "Leu",
    "lüsiin": "Lys", "metioniin": "Met", "fenüülalaniin": "Phe", "proliin": "Pro",
    "seriin": "Ser", "treoniin": "Thr", "trüptofaan": "Trp", "tsüsteiin": "Cys",
    "türosiin": "Tyr", "valiin": "Val", "selenotsüsteiin": "Sec", "pürrolüsiin": "Pyl"}
sonastik_keskmine = {"alaniin": "A", "arginiin": "R", "asparagiin": "N",
    "asparagiinhape": "D", "glutamiin": "Q", "glutamiinhape": "E", "glütsiin": "G",
    "Histidiin": "H", "Isoleutsiin": "I", "Leutsiin": "L", "Lüsiin": "K", "Metioniin": "M",
    "fenüülalaniin": "F", "proliin": "P", "seriin": "S", "treoniin": "T", "trüptofaan": "W",
    "tsüsteiin": "C", "türosiin": "Y", "valiin": "V", "selenotsüsteiin": "U",
                   "pürrolüsiin": "O"}

# see funktsioon käivitatakse nupule klõpsamisel
def raskusaste():
    if v.get()== 1:
        print("kas töötab?")
        sonastik = sonastik_lihtsam
        print(sonastik)
    elif v.get() == 2:
        print("vist töötab")
        sonastik = sonastik_keskmine
        print(sonastik)
    elif v.get() == 3:
        return
        #ei muuda midagi
    #teen tahvli tühjaks
    tahvel.delete("all")
    nupp.place_forget()
    global nupp1
    global nupp2
    global nupp3
    nupp1.destroy()
    nupp2.destroy()
    nupp3.destroy()

# loome akna
raam = Tk()
raam.title("Aminohapete mäng")
#raam.geometry("550x300")
tahvel = Canvas(raam, width= 550, height= 300)
tahvel.grid()

#aminohappe pilt tahvlile
normaal_suurus = Image.open("pildid/aminohape.png")
muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
aminohape = ImageTk.PhotoImage(muudetud)
pilt = tahvel.create_image(175, 100, anchor = W, image= aminohape)

#radiobutton
v = IntVar()
#IntVar (või StringVar) väärtuseks on hetkel valitud radiobuttoni value.
#Selle järgi saab kindlaks teha, milline on valitud.
#Submit nupp on tavaline nupp. Peale submit vajutamist kontrollid IntVar väärtust.

#Iga nupp on kahel real, et saaksin kasutada destroy() käsku
nupp1 = Radiobutton(raam, text="Kerge", variable=v, value=1)
nupp1.grid(row=1)
nupp2 = Radiobutton(raam, text="Keskmine", variable=v, value=2)
nupp2.grid(row=2)
nupp3 = Radiobutton(raam, text="Raske", variable=v, value=3)
nupp3.grid(row=3)

# loome nupu
nupp = ttk.Button(raam, text="Valmis", command=raskusaste)
#Button(raam, text="Tervita!", command=lambda: tervita(argument))
nupp.place(x=200, y=200, width=150)

# ilmutame akna ekraanile
raam.mainloop()
