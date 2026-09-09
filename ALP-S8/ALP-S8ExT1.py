# Imports
from turtle import *
# Constantes



# Procédures et fonctions
def entree():
    longeur = int(input("Longeur initial : "))
    increment = int(input("Increment : "))
    longeur_max = int(input("Longeur max : "))
     
    return longeur,increment,longeur_max

def dessiner(longeur,longeur_max,increment):
    speed(-1)
    while longeur <= longeur_max:
        fd(longeur)
        right(90)
        longeur+=increment
        
# Procédure main()
def main():
    longeur,increment,longeur_max = entree()
    dessiner(longeur,longeur_max,increment)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

