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

silt1 = ttk.Label(raam, text="Oled avanud aminohapete mängu!", font=suur_font, background= "white")
silt1.place(x=110,y=1)
silt2 = ttk.Label(raam, text= "Mängida on võimalik erinevatel raskustasemetel. Kui soovid valida valikvastustega versiooni, "
                              , background= "white")
silt2.place(x=30, y=30)
silt3 = ttk.Label(raam, text= "vajuta nuppu xxx. Soovides mängida xxx, vajuta nupule xxx", background="white")
silt3.place(x=80, y=50)

vasak_nupp = ttk.Button(raam, text="Vajuta mind", command= fn_valikvastused)
vasak_nupp.place(x= 50, y= 150, width=100)

parem_nupp = ttk.Button(raam, text="Vajuta mind ka", command= raskusastmed_fn)
parem_nupp.place(x= 200, y= 150, width=100)

raam.mainloop()