# Imports
from turtle import *
# Constantes
MIN = 3


# Procédures et fonctions
def dessiner_triangle(cote,increment):
    
    for i in range(increment):
        forward(cote)
        left(120)
   
    
    
def spirale_triangles(cote,increment):
    
    if cote < 3:
        return
    
    dessiner_triangle(cote,increment)

    forward(cote)
    left(120)
        
    fd(cote)
    right(60)
    increment+=1
    spirale_triangles(cote/2,increment)
    
def main():
    increment = 4
    # Demande de la longueur initiale à l'utilisateur
    longueur_initiale = float(input("Entrez la longueur du côté initial : "))
    
    spirale_triangles(longueur_initiale,increment)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()


