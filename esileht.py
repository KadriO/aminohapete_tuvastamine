__author__ = 'Kadri'

from tkinter import *
from tkinter import ttk
from tkinter import font
from fn_valikvastused import fn_valikvastused
from raskusastmed_funktsioon import raskusastmed_fn

raam = Tk()
raam.title("Aminohapete mäng")
tahvel = Canvas(raam, width= 550, height= 300, background= "white")
tahvel.grid()

suur_font = font.Font(family='Times', size=14, weight='bold')

silt1 = ttk.Label(raam, text="Aminohapete mäng", font=suur_font, background= "white")
silt1.place(x=200,y=30)
silt2 = ttk.Label(raam, text= "Mängida on võimalik nii sisestades aminohappe nime (kolme erineva raskustasemega), kui \
ka valides kolme erineva valikvastuse vahel. Klikates nuppu \"Valikvastused\" alustad valikvastustega mängu mängimist\
 ning klikates nuppu \"Tekstisisestus\" alustad mängu, kus tuleb trükkida õige aminohappe nimi. "
                              , background= "white", wraplength = 500)
silt2.place(x=30, y=70)
#silt3 = ttk.Label(raam, text= "vajuta nuppu xxx. Soovides mängida xxx, vajuta nupule xxx", background="white")
#silt3.place(x=80, y=50)

vasak_nupp = ttk.Button(raam, text="Valikvastused", command= fn_valikvastused)
vasak_nupp.place(x= 150, y= 160, width=100)

parem_nupp = ttk.Button(raam, text="Tekstisisestus", command= raskusastmed_fn)
parem_nupp.place(x= 300, y= 160, width=100)

raam.mainloop()