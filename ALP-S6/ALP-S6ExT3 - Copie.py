# Imports
from turtle import *
# Constantes

# Procédures et fonctions
def dessiner_croix(taille):
    for i in range(4):
        for c in ('blue','red'):
            color(c)             #
            forward(taille)      #
            dot(20)              #
            back(taille)         # Tu peut sortir ce code si tu veut juste faire en bleu
            dot(10)              #
            left(90)             #
            
# Procédure main()
def main():
    
    taille = int(input("Entrez la taille d'une des branche de la croix:"))
    
    dessiner_croix(taille)
    
    exitonclick()

# Appel de la procédure main()
if __name__ == "__main__":
    main()