#hetkel veel raskusastme osa poolik, aga lõpetan selle siis, kui muu programmi osa saan tööle

# impordi tk vidinad ja konstandid
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Raskuksastmed, kõige raskema puhul vihjeid ei pane, kergemal tasemel on vihjeks/
#aminohappe kolmetäheline lühend, keskmisel ühetäheline
sonastik = {}
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
    global sonastik
    if v.get()==1:
        sonastik = sonastik_lihtsam
    elif v.get() == 2:
        sonastik = sonastik_keskmine
    elif v.get() == 3:
        return
        #ei muuda midagi


# loome akna
raam = Tk()
raam.title("Aminohapete mäng")
raam.geometry("550x300")
tahvel = Canvas(raam, width= 550, height= 300, background = "white")
#tahvel.grid()

#radiobutton
v = IntVar()
#IntVar (või StringVar) väärtuseks on hetkel valitud radiobuttoni value.
#Selle järgi saab kindlaks teha, milline on valitud.
#Submit nupp on tavaline nupp. Peale submit vajutamist kontrollid IntVar väärtust.

Radiobutton(raam, text="Kerge", variable=v, value=1).grid(row=1, sticky=(W))
Radiobutton(raam, text="Keskmine", variable=v, value=2).grid(row=2, sticky=(W))
Radiobutton(raam, text="Raske", variable=v, value=3).grid(row=3, sticky=(W))

#aminohappe pilt panna

# loome nupu
nupp = ttk.Button(raam, text="Valmis", command=raskusaste)
#Button(raam, text="Tervita!", command=lambda: tervita(argument))
nupp.place(x=10, y=100, width=150)

# ilmutame akna ekraanile
raam.mainloop()
