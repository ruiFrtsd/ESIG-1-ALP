# Imports
import math
# Constantes

# Procédures et fonctions
def entree():
    rayon = float(input("Entrez un rayon"))
    return rayon

def calculer_cercle(rayon):
    aire = math.pi * (rayon * rayon)
    circonference = 2 * math.pi * rayon
    return aire,circonference

# Procédure main()
def main():
    #entree
    rayon = entree()
    #calcul
    aire,circonference = calculer_cercle(rayon)
    #sortie
    print("Un cercle de rayon ", rayon , " a une aire de ", aire , " et une circonference de ", circonference)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

