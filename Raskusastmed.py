#programm Ahto, hetkel veel raskusastme osa poolik, aga lõpetan selle siis, kui muu programmi osa saan tööle

# impordi tk vidinad ja konstandid
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# see funktsioon käivitatakse nupule klõpsamisel
def raskusaste(v):
    #Raskuksastmed, kõige raskema puhul vihjeid ei pane, kergemal tasemel on vihjeks/
    #aminohappe kolmetäheline lühend, keskmisel ühetäheline
    sonastik_lihtsam ={"alaniin": "Ala", "arginiin": "Arg", "asparagiin": "Asn"\
    , "asparagiinhape": "Asp", "Glutamiin": "Gln", "Glutamiinhape": "Glu", \
    "glütsiin": "Gly", "histidiin": "His", "isoleutsiin": "Ile", "leutsiin": "Leu",\
    "lüsiin": "Lys", "metioniin": "Met", "fenüülalaniin": "Phe", "proliin": "Pro",\
    "seriin": "Ser", "treoniin": "Thr", "trüptofaan": "Trp", "tsüsteiin": "Cys", \
    "türosiin": "Tyr", "valiin": "Val", "selenotsüsteiin": "Sec", "pürrolüsiin": "Pyl"}
    sonastik_keskmine = {"alaniin": "A", "arginiin": "R", "asparagiin": "N",\
    "asparagiinhape": "D", "glutamiin": "Q", "glutamiinhape": "E", "glütsiin": "G", \
    "Histidiin": "H", "Isoleutsiin": "I", "Leutsiin": "L", "Lüsiin": "K", "Metioniin": "M",\
    "fenüülalaniin": "F", "proliin": "P", "seriin": "S", "treoniin": "T", "trüptofaan": "W", \
    "tsüsteiin": "C", "türosiin": "Y", "valiin": "V", "selenotsüsteiin": "U", \
                   "pürrolüsiin": "O"}
    if v == 1:
        return sonastik_lihtsam
    elif v == 2:
        return sonastik_keskmine
    elif v == 3:
        return
    
# loome akna
raam = Tk()
raam.title("Aminohapete mäng")
raam.geometry("640x480")

#radiobutton
v = IntVar()

Radiobutton(raam, text="Kerge", variable=v, value=1).pack(anchor=W)
Radiobutton(raam, text="Keskmine", variable=v, value=2).pack(anchor=W)
Radiobutton(raam, text="Raske", variable=v, value=3).pack(anchor=W)

# loome nupu
nupp = ttk.Button(raam, text="Valmis", command=raskusaste(v))
nupp.place(x=10, y=100, width=150)

# ilmutame akna ekraanile
raam.mainloop()
