__author__ = 'Kadri'

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint

#rea numbri määramine radio nuppude jaoks
def rea_numbrite_leidmine():
    global rea_numbrid
    #teen eelneva listi tühjaks
    del rea_numbrid[:]
    while True:
        rea_number = randint(1,3)
        if rea_number not in rea_numbrid:
            rea_numbrid.append(rea_number)
        if len(rea_numbrid)==3:
            return rea_numbrid

def esimene_vastusevariant():
    global ah_number
    while True:
        esimene_number = randint(0, len(aminohapped)-1)
        if esimene_number != ah_number:
            esimene_valik = aminohapped[esimene_number]
            return esimene_valik, esimene_number

def teine_vastusevariant():
    global ah_number
    global esimene_number
    while True:
        teine_number = randint(0, len(aminohapped)-1)
        if teine_number != ah_number and teine_number != esimene_number:
            teine_valik = aminohapped[teine_number]
            return teine_valik

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
    #global teine_number
    global nupp_1
    global nupp_2
    global nupp_3
    global v
    global rea_numbrid
    v = StringVar()
    #loob uued valikvastused
    esimene_valik, esimene_number = esimene_vastusevariant()
    teine_valik = teine_vastusevariant()
    #kustutab eelnevad vastusevariandid ära
    nupp_1.destroy()
    nupp_2.destroy()
    nupp_3.destroy()
    rea_numbrid = rea_numbrite_leidmine()
    #lisab uued vastusevariandid
    nupp_1 = Radiobutton(raam, text=esimene_valik, variable = v, value=esimene_valik)
    nupp_1.grid(row=rea_numbrid[0], sticky=(N))
    nupp_2 = Radiobutton(raam, text=teine_valik, variable = v, value=teine_valik)
    nupp_2.grid(row=rea_numbrid[1], sticky=(N))
    nupp_3 = Radiobutton(raam, text=ah_nimi, variable = v, value=ah_nimi)
    nupp_3.grid(row=rea_numbrid[2], sticky=(N))

def vaheta_aminohape2():
    global aminohape
    global ah_number
    global ah_nimi
    global valitud_aminohapped
    while True:
        ah_number = randint(0, len(aminohapped)-1)
        ah_nimi = aminohapped[ah_number]
        if ah_nimi not in valitud_aminohapped:
            break
    valitud_aminohapped.append(ah_nimi)
    print(ah_nimi)
    #print(ah_number)
    #print(valitud_aminohapped)
    normaal_suurus = Image.open("pildid/"+ah_nimi+".png")
    muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
    aminohape = ImageTk.PhotoImage(muudetud)
    tahvel.itemconfigure(pilt, image=aminohape)

    vaheta_valikvastused()

def salvesta_vastus():
    global nupp_1
    global nupp_2
    global nupp_3
    tulemus = vastuse_kontroll()
    if len(tulemused)<=9:
        if tulemus == False:
            tulemused.append(0)
        else:
            tulemused.append(1)
        vaheta_aminohape2()
    if len(tulemused)==10:
        tahvel.delete("all")
        nupp.place_forget()
        nupp_1.destroy()
        nupp_2.destroy()
        nupp_3.destroy()
        silt3 = Label(raam, background="white", text="Mäng on läbi!")
        silt3.place(x=160, y=80)
        silt2 = Label(raam, background="white", text="Sinu skoor on "+ \
        str(tulemused.count(1))+"/"+str(tulemused.count(0)+tulemused.count(1)))
        silt2.place(x=150, y=100)
    print(tulemused)

def fn_valikvastused():
    global raam
    raam = Toplevel()
    raam.title("Aminohapete mäng")
    global tahvel
    tahvel = Canvas(raam, width= 400, height= 200, background = "white")
    tahvel.grid()

    global aminohapped
    aminohapped = ["alaniin", "arginiin", "asparagiin", "asparagiinhape", "tsüsteiin", "glutamiin", "glutamiinhape", "glütsiin",
    "histidiin", "isoleutsiin", "leutsiin", "lüsiin", "metioniin", "fenüülalaniin", "proliin", "seriin",
    "treoniin", "trüptofaan", "türosiin", "valiin", "selenotsüsteiin", "pürrolüsiin"]

    global tulemused
    tulemused = []
    global rea_numbrid
    rea_numbrid = []
    global valitud_aminohapped
    valitud_aminohapped = []

    #Pildi kuvamine
    global ah_nimi
    global ah_number
    ah_number = randint(0, len(aminohapped)-1)
    ah_nimi = aminohapped[ah_number]
    valitud_aminohapped.append(ah_nimi)
    print(ah_nimi)
    #print(ah_number)
    #print(valitud_aminohapped)

    global aminohape
    normaal_suurus = Image.open("pildid/"+ah_nimi+".png")
    muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
    aminohape = ImageTk.PhotoImage(muudetud)
    global pilt
    pilt = tahvel.create_image(100, 100, anchor = W, image= aminohape)

    #Kahe aminohappe määramine valikvastuseks
    global v
    v = StringVar()

    global esimene_valik
    global esimene_number
    global teine_valik
    esimene_valik, esimene_number = esimene_vastusevariant()
    teine_valik = teine_vastusevariant()

    #global rea_numbrid
    rea_numbrid = rea_numbrite_leidmine()
    #Valikvastused
    global nupp_1
    nupp_1 = Radiobutton(raam, text=esimene_valik, variable = v, value=esimene_valik)
    nupp_1.grid(row=rea_numbrid[0], sticky=(N))
    global nupp_2
    nupp_2 = Radiobutton(raam, text=teine_valik, variable = v, value=teine_valik)
    nupp_2.grid(row=rea_numbrid[1], sticky=(N))
    global nupp_3
    nupp_3 = Radiobutton(raam, text=ah_nimi, variable = v, value=ah_nimi)
    nupp_3.grid(row=rea_numbrid[2], sticky=(N))

    global nupp
    nupp = ttk.Button(raam, text="Edasi", command = salvesta_vastus)
    nupp.place(x=270, y=220, width=100)

    raam.mainloop()