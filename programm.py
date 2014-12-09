__author__ = 'Ahto'
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint
from time import sleep

def fn_kontrolli(sisestus, ah_nimi):
    vastus = False
    if sisestus == ah_nimi:
        vastus = True
    return vastus

#hetkel veel ajaloendurit pole kasutanud
def ajaloendur(piiratud_aeg) :
    if piiratud_aeg == 0:
        return True
    else:
        print(piiratud_aeg)
        sleep(1) # ootab 1 sekundi
        ajaloendur(piiratud_aeg-1)

#funktsioon vahetab aminohappe pildi

def vaheta_aminohape():
    global aminohape
    ah_number = randint(0, len(aminohapped)-1)
    ah_nimi = aminohapped[ah_number]
    normaal_suurus = Image.open(ah_nimi+".png")
    muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
    aminohape = ImageTk.PhotoImage(muudetud)
    tahvel.itemconfigure(pildi_id, image=aminohape)
    return ah_number

def uuenda2(ajalimiit):
    tagasiside = ajaloendur(ajalimiit)
    if tagasiside == True:
        vaheta_aminohape()


def salvesta():
    sisestus = ah_lahter.get()
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
        silt = Label(raam, background="white", text="Mäng on läbi!")
        silt.place(x=230, y=110)
        silt2 = Label(raam, background="white", text="Sinu skoor on "+ \
        str(tulemused.count(1))+"/"+str(tulemused.count(0)+tulemused.count(1)))
        silt2.place(x=220, y=140)

        #if "valed_vastused" not in tulemused:
            #tulemused["valed_vastused"] = 1
        #else:
            #tulemused["valed_vastused"] += 1
    #else:
        #if "oiged_vastused" not in tulemused:
            #tulemused["oiged_vastused"] = 1
        #else:
            #tulemused["oiged_vastused"] += 1
    print(tulemused)
    ah_number = vaheta_aminohape()
    #return ah_number

aminohapped = ["alaniin", "arginiin", "asparagiin"]

def uuenda():
    tahvel.delete(pildi_id)
    ah_number = randint(0, len(aminohapped)-1)
    ah_nimi = aminohapped[ah_number]
    print(ah_nimi)
    print(ah_number)

    normaal_suurus = Image.open(ah_nimi+".png")
    muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
    aminohape = ImageTk.PhotoImage(muudetud)

    pildi_id = tahvel.create_image(30, 130, anchor = W, image= aminohape)

    raam.after(3000, uuenda)

#i = 0
#while i < 10:

raam = Tk()
raam.title("Aminohapete mäng")
tahvel = Canvas(raam, width= 550, height= 300, background = "white")
tahvel.grid()
#uuenda()
#aminohapped = ["alaniin", "arginiin", "asparagiin", "asparagiinhape", "tsüteiin", "glutamiin", "glutamiinhape", "glütsiin",
#"histidiin", "isoleutsiin", "leutsiin", "lüsiin", "metioniin", "fenüülalaniin", "proliin", "seriin",
#"treoniin", "trüptofaan", "türosiin", "valiin", "selenotsüsteiin", "pürrolüsiin"]
#aminohapped = ["alaniin", "arginiin", "asparagiin"]
tulemused = []

ah_number = randint(0, len(aminohapped)-1)
ah_nimi = aminohapped[ah_number]
print(ah_nimi)
print(ah_number)

normaal_suurus = Image.open(ah_nimi+".png")
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
#nupp = ttk.Button(raam, text="Salvesta vastus", command = vaheta_aminohape)
nupp = ttk.Button(raam, text="Salvesta vastus", command = salvesta)
nupp.place(x=330, y=170, width=100)
raam.mainloop()



