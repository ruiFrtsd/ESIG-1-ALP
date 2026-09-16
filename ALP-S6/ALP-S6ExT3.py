# Imports
from turtle import *
# Constantes

# Procédures et fonctions
def dessiner_croix(taille):
    for i in range(4):
        color('blue')             
        forward(taille)      
        dot(20)              
        back(taille)
        dot(10)              
        left(90)             
            
# Procédure main()
def main():
    taille = int(input("Entrez la taille d'une des branche de la croix:"))
    
    dessiner_croix(taille)

# Appel de la procédure main()
if __name__ == "__main__":
    main()