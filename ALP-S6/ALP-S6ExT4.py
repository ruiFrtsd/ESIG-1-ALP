# Imports
from turtle import *
# Constantes

# Procédures et fonctions
def dessiner_croix(taille):
    for i in range(taille):
        dot(10)
        if i % 2 == 0 :
            left
# Procédure main()
def main():
    
    taille = int(input("Entrez la taille d'une des branche de la croix:"))
    
    dessiner_zigzag(taille)


# Appel de la procédure main()
if __name__ == "__main__":
    main()
