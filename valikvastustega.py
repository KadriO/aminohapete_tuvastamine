__author__ = 'Kadri'

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint

def vastuse_kontroll():
    global v
    global ah_nimi
    vastus = False
    if v.get() == ah_nimi:
        vastus = True
    return vastus

def vaheta_valikvastused():
    global ah_nimi
    global esimene_valik
    global esimene_number
    global teine_valik
    global teine_number
    global nupp_1
    global nupp_2
    global nupp_3
    global v
    v = StringVar()
    esimene_number = randint(0, len(aminohapped)-1)
    if esimene_number == ah_number:
        esimene_number = randint(0, len(aminohapped)-1)
    esimene_valik = aminohapped[esimene_number]
    teine_number = randint(0, len(aminohapped)-1)
    if teine_number == ah_number or teine_number == esimene_number:
        teine_number = randint(0, len(aminohapped)-1)
    teine_valik = aminohapped[teine_number]
    nupp_1.destroy()
    nupp_2.destroy()
    nupp_3.destroy()
    nupp_1 = Radiobutton(raam, text=esimene_valik, variable = v, value=esimene_valik)
    nupp_1.grid(row=1, sticky=(N))
    nupp_2 = Radiobutton(raam, text=teine_valik, variable = v, value=teine_valik)
    nupp_2.grid(row=2, sticky=(N))
    nupp_3 = Radiobutton(raam, text=ah_nimi, variable = v, value=ah_nimi)
    nupp_3.grid(row=3, sticky=(N))

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
    tahvel.itemconfigure(pilt, image=aminohape)

    vaheta_valikvastused()

def salvesta_vastus():
    tulemus = vastuse_kontroll()
    if len(tulemused)<=9:
        if tulemus == False:
            tulemused.append(0)
        else:
            tulemused.append(1)
        vaheta_aminohape()
    if len(tulemused)==10:
        tahvel.delete("all")
        nupp.place_forget()
        #nende nuppude kustutamine ei tööta
        global nupp_1
        global nupp_2
        global nupp_3
        nupp_1.destroy()
        nupp_2.destroy()
        nupp_3.destroy()
        silt3 = Label(raam, background="white", text="Mäng on läbi!")
        silt3.place(x=230, y=110)
        silt2 = Label(raam, background="white", text="Sinu skoor on "+ \
        str(tulemused.count(1))+"/"+str(tulemused.count(0)+tulemused.count(1)))
        silt2.place(x=220, y=140)
    print(tulemused)


raam = Tk()
raam.title("Aminohapete mäng")
tahvel = Canvas(raam, width= 400, height= 200, background = "white")
tahvel.grid()

aminohapped = ["alaniin", "arginiin", "asparagiin", "asparagiinhape", "tsüsteiin", "glutamiin", "glutamiinhape", "glütsiin",
"histidiin", "isoleutsiin", "leutsiin", "lüsiin", "metioniin", "fenüülalaniin", "proliin", "seriin",
"treoniin", "trüptofaan", "türosiin", "valiin", "selenotsüsteiin", "pürrolüsiin"]

tulemused = []

#Pildi kuvamine
ah_number = randint(0, len(aminohapped)-1)
ah_nimi = aminohapped[ah_number]
print(ah_nimi)
print(ah_number)

normaal_suurus = Image.open("pildid/"+ah_nimi+".png")
muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
aminohape = ImageTk.PhotoImage(muudetud)
pilt = tahvel.create_image(100, 100, anchor = W, image= aminohape)

#Kahe aminohappe määramine valikvastuseks
v = StringVar()
esimene_number = randint(0, len(aminohapped)-1)
esimene_valik = aminohapped[esimene_number]

teine_number = randint(0, len(aminohapped)-1)
teine_valik = aminohapped[teine_number]

#Valikvastused
nupp_1 = Radiobutton(raam, text=esimene_valik, variable = v, value=esimene_valik)
nupp_1.grid(row=1, sticky=(N))
nupp_2 = Radiobutton(raam, text=teine_valik, variable = v, value=teine_valik)
nupp_2.grid(row=2, sticky=(N))
nupp_3 = Radiobutton(raam, text=ah_nimi, variable = v, value=ah_nimi)
nupp_3.grid(row=3, sticky=(N))

nupp = ttk.Button(raam, text="Edasi", command = salvesta_vastus)
nupp.place(x=270, y=220, width=100)

raam.mainloop()