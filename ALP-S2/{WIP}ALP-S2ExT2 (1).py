# Imports
from turtle import *
# Constantes
DEGRES_CARRE = 90
DEGRES_TRIANGLE = 120
DEGRES_PENTA = 72
DEGRES_ROND = 1

FACES_CARRE = 4
FACES_TRIANGLE = 3
FACES_PENTA = 5
FACES_ROND = 360
# Procédures et fonctions
def questionTime():
    forme = int(input("Quel est le nombre de coté souhaité ? (Carré[4], Triangle[3] ou Pentagone[5]) :"))
    perimetre = int(input("Quel est le perimetre de la forme?"))
    quelForme(forme,perimetre)

def quelForme(forme,perimetre):
    if forme == FACES_CARRE :
        dessineCarre(perimetre)
    elif forme == FACES_TRIANGLE:
        dessineTriangle(perimetre)
    elif forme == FACES_PENTA :
        dessinePentagone(perimetre)
    elif forme == FACES_ROND:
        dessineRond(perimetre)
    else:
        print("Forme inconnu ou non completable")
        main()
        
def dessineCarre(perimetre):
    for i in range(FACES_CARRE):
        forward(perimetre/FACES_CARRE)
        left(DEGRES_CARRE)
        
def dessineTriangle(perimetre):
    for i in range(FACES_TRIANGLE):
        forward(perimetre/FACES_TRIANGLE)
        left(DEGRES_TRIANGLE)

def dessinePentagone(perimetre):
    for i in range(FACES_PENTA):
        forward(perimetre/FACES_PENTA)
        left(DEGRES_PENTA)

def dessineRond(perimetre):
    for i in range(FACES_ROND):
        forward(perimetre/FACES_ROND)
        left(DEGRES_ROND)
# Procédure main()
def main():
    questionTime()
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
