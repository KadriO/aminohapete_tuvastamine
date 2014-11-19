__author__ = 'Kadri'
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint
from funktsioonid import fn_kontrolli

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width= 550, height= 300, background = "white")
tahvel.grid()

aminohapped = ["alaniin", "arginiin", "asparagiin", "asparagiinhape", "tsüteiin", "glutamiin", "glutamiinhape", "glütsiin",
               "histidiin", "isoleutsiin", "leutsiin", "lüsiin", "metioniin", "fenüülalaniin", "proliin", "seriin",
               "treoniin", "trüptofaan", "türosiin", "valiin", "selenotsüsteiin", "pürrolüsiin"]

tulemused = {}
def salvesta():
    sisestus = ah_lahter.get()
    tulemus = fn_kontrolli(sisestus.lower(), ah_nimi)
    if tulemus == False:
        if "valed_vastused" not in tulemused:
            tulemused["valed_vastused"] = 1
        else:
            tulemused["valed_vastused"] += 1
    else:
        if "oiged_vastused" not in tulemused:
            tulemused["oiged_vastused"] = 1
        else:
            tulemused["oiged_vastused"] += 1
    print(tulemused)

ah_number = randint(0, len(aminohapped)-1)
ah_nimi = aminohapped[ah_number]
print(ah_nimi)
print(ah_number)

normaal_suurus = Image.open("pildid/"+ah_nimi+".png")
muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
aminohape = ImageTk.PhotoImage(muudetud)
pildi_id = tahvel.create_image(30, 130, anchor = W, image= aminohape)

#sildi tegemine:
silt = Label(raam, background="white", text="Kirjuta aminohappe nimi:")
silt.place(x=300, y=110)

#tekstikasti tegemine:
ah_lahter = ttk.Entry(raam)
ah_lahter.place(x=300, y=130, width=150)

#nupp:
nupp = ttk.Button(raam, text="Salvesta vastus", command = salvesta)
nupp.place(x=330, y=170, width=100)


raam.mainloop()