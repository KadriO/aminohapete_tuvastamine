from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#from tkinter import messagebox
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
    #teeb lahtri tühjaks
    ah_lahter_id.delete(0, END)

    global vihje
    global sonastik
    global vihje_silt
    if vihje == True:
        vihje_silt.place_forget()
        vihje_sone = sonastik[ah_nimi]
        vihje_silt = Label(raam, background="white", text="Vihje: "+vihje_sone)
        vihje_silt.place(x=300, y=200)


def salvesta():
    sisestus = ah_lahter_id.get()
    tulemus = fn_kontrolli(sisestus.lower(), ah_nimi)
    if len(tulemused)<=9:
        if tulemus == False:
            tulemused.append(0)
        else:
            tulemused.append(1)
        vaheta_aminohape()
    if len(tulemused)==10:
        #global vihje
        global vihje_silt
        #teeb tahvli tühjaks
        tahvel.delete("all")
        nupp.place_forget()
        silt.place_forget()
        ah_lahter_id.place_forget()
        if vihje == True:
            vihje_silt.place_forget()
        #lisab tahvlile uue sisu
        silt3 = Label(raam, background="white", text="Mäng on läbi!")
        silt3.place(x=230, y=110)
        silt2 = Label(raam, background="white", text="Sinu skoor on "+ \
        str(tulemused.count(1))+"/"+str(tulemused.count(0)+tulemused.count(1)))
        silt2.place(x=220, y=140)
    print(tulemused)
    #if len(tulemused)<=9:
        #vaheta_aminohape()

def põhi_programm():
    global ah_number
    global ah_nimi
    ah_number = randint(0, len(aminohapped)-1)
    ah_nimi = aminohapped[ah_number]
    print(ah_nimi)
    print(ah_number)

    global vihje
    global vihje_silt
    if vihje == True:
        global sonastik
        vihje_sone = sonastik[ah_nimi]
        vihje_silt = Label(raam, background="white", text="Vihje: "+vihje_sone)
        vihje_silt.place(x=300, y=200)

    global pildi_id
    global aminohape
    normaal_suurus = Image.open("pildid/"+ah_nimi+".png")
    muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
    aminohape = ImageTk.PhotoImage(muudetud)
    pildi_id = tahvel.create_image(30, 130, anchor = W, image= aminohape)

#sildi tegemine:
    global silt
    silt = Label(raam, background="white", text="Kirjuta aminohappe nimi:")
    silt.place(x=300, y=110)

#tekstikasti tegemine:
    global ah_lahter_id
    ah_lahter_id = ttk.Entry(raam)
    ah_lahter_id.place(x=300, y=130, width=150)
#nupp:
    global nupp
    nupp = ttk.Button(raam, text="Salvesta vastus", command = salvesta)
    nupp.place(x=330, y=170, width=100)
    #pildi_id.pack()

# see funktsioon käivitatakse nupule klõpsamisel
def raskusaste():
    global vihje
    global sonastik
    if v.get()== 1:
        vihje = True
        print("kas töötab?")
        sonastik = sonastik_lihtsam
        print(sonastik)
    elif v.get() == 2:
        vihje = True
        print("vist töötab")
        sonastik = sonastik_keskmine
        print(sonastik)
    elif v.get() == 3:
        vihje = False
        sonastik = sonastik  #prooviks
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
    põhi_programm()

aminohapped = ["alaniin", "arginiin", "asparagiin", "asparagiinhape", "tsüsteiin", "glutamiin", "glutamiinhape", "glütsiin",
"histidiin", "isoleutsiin", "leutsiin", "lüsiin", "metioniin", "fenüülalaniin", "proliin", "seriin",
"treoniin", "trüptofaan", "türosiin", "valiin", "selenotsüsteiin", "pürrolüsiin"]

#Raskusastmed, kõige raskema puhul vihjeid ei pane, kergemal tasemel on vihjeks/
#aminohappe kolmetäheline lühend, keskmisel ühetäheline
sonastik = {}
sonastik_lihtsam ={"alaniin": "Ala", "arginiin": "Arg", "asparagiin": "Asn"
    , "asparagiinhape": "Asp", "glutamiin": "Gln", "glutamiinhape": "Glu",
    "glütsiin": "Gly", "histidiin": "His", "isoleutsiin": "Ile", "leutsiin": "Leu",
    "lüsiin": "Lys", "metioniin": "Met", "fenüülalaniin": "Phe", "proliin": "Pro",
    "seriin": "Ser", "treoniin": "Thr", "trüptofaan": "Trp", "tsüsteiin": "Cys",
    "türosiin": "Tyr", "valiin": "Val", "selenotsüsteiin": "Sec", "pürrolüsiin": "Pyl"}
sonastik_keskmine = {"alaniin": "A", "arginiin": "R", "asparagiin": "N",
    "asparagiinhape": "D", "glutamiin": "Q", "glutamiinhape": "E", "glütsiin": "G",
    "histidiin": "H", "isoleutsiin": "I", "leutsiin": "L", "lüsiin": "K", "metioniin": "M",
    "fenüülalaniin": "F", "proliin": "P", "seriin": "S", "treoniin": "T", "trüptofaan": "W",
    "tsüsteiin": "C", "türosiin": "Y", "valiin": "V", "selenotsüsteiin": "U",
                   "pürrolüsiin": "O"}

tulemused = []
ah_nimi = ""
ah_number = ""

# loome akna
raam = Tk()
raam.title("Aminohapete mäng")
tahvel = Canvas(raam, width= 550, height= 300, background= "white")
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



