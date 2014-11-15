__author__ = 'Kadri'
from tkinter import *
from PIL import Image, ImageTk
from random import randint

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width= 300, height= 300, background = "white")
tahvel.grid()

aminohapped = ["alanine", "arginine", "asparagine", "aspartic_acid", "cysteine", "glutamine", "glutamic_acid", "glycine",
               "histidine", "isoleucine", "leucine", "lysine", "methionine", "phenylalanine", "proline", "serine",
               "threonine", "tryptophan", "tyrosine", "valine", "selenocysteine", "pyrrolysine"]

ah_number = randint(0, len(aminohapped)-1)
ah_nimi = aminohapped[ah_number]
print(ah_number)

normaal_suurus = Image.open("pildid/"+ah_nimi+".png")
muudetud = normaal_suurus.resize((200,150),Image.ANTIALIAS)
aminohape = ImageTk.PhotoImage(muudetud)
pilt = tahvel.create_image(50, 90, anchor = W, image= aminohape)

raam.mainloop()