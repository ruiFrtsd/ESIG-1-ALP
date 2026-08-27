from turtle import *
forme = str(input("Entrez une forme (Carré ou Ligne): "))

if forme.lower() == "carré" or forme.lower() == "carre" :
    nPremier = int(input("Entrer nombre premier : "))
    for i in range(4) :
        right(90)
        forward(nPremier)   
elif forme.lower() == "ligne" :
    nPremier = int(input("Entrer nombre premier : "))
    forward(nPremier)
else :
    print("Forme inconnu")