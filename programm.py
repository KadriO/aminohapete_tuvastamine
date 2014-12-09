__author__ = 'Ahto'
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint


def fn_kontrolli(sisestus, ah_nimi):
    vastus = False
    if sisestus == ah_nimi:
        vastus = True
    return vastus

#funktsioon vahetab aminohappe pildi
def vaheta_aminohape():
    global aminohape
    global ah_number
    global ah_nimi
    ah_number = randint(0, len(aminohapped)-1)
    ah_nimi = aminohapped[ah_number]
    print(ah_nimi)
    print(ah_number)
    normaal_suurus = Image.open("pildid/"+ah_nimi+".png")
    muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
    aminohape = ImageTk.PhotoImage(muudetud)
    tahvel.itemconfigure(pildi_id, image=aminohape)

    ah_lahter_id.delete(0, END)


def salvesta():
    sisestus = ah_lahter_id.get()
    tulemus = fn_kontrolli(sisestus.lower(), ah_nimi)
    if len(tulemused)<10:
        if tulemus == False:
            tulemused.append(0)
        else:
            tulemused.append(1)
    else:
        #siinmail peaks kuidagi ära lõpetama, nt kirjutama skoori
        raam = Tk()
        raam.title("Aminohapete mäng")
        tahvel = Canvas(raam, width= 550, height= 300, background = "white")
        tahvel.grid()
        #kustutada ah_pilt, kustutada nupp, kustutada, kustutada silt, kustutada lahter
        silt = Label(raam, background="white", text="Mäng on läbi!")
        silt.place(x=230, y=110)
        silt2 = Label(raam, background="white", text="Sinu skoor on "+ \
        str(tulemused.count(1))+"/"+str(tulemused.count(0)+tulemused.count(1)))
        silt2.place(x=220, y=140)

    print(tulemused)
    vaheta_aminohape()


#Programm
raam = Tk()
raam.title("Aminohapete mäng")
tahvel = Canvas(raam, width= 550, height= 300, background = "white")
tahvel.grid()

aminohapped = ["alaniin", "arginiin", "asparagiin", "asparagiinhape", "tsüteiin", "glutamiin", "glutamiinhape", "glütsiin",
"histidiin", "isoleutsiin", "leutsiin", "lüsiin", "metioniin", "fenüülalaniin", "proliin", "seriin",
"treoniin", "trüptofaan", "türosiin", "valiin", "selenotsüsteiin", "pürrolüsiin"]

tulemused = []

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
ah_lahter_id = ttk.Entry(raam)
ah_lahter_id.place(x=300, y=130, width=150)
#nupp:
nupp = ttk.Button(raam, text="Salvesta vastus", command = salvesta)
nupp.place(x=330, y=170, width=100)
raam.mainloop()