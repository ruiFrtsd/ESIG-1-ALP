# Imports

# Constantes

# Procédures et fonctions
def positifOuNegatif(nEntier) :
    if nEntier > 0 :
        print("Le nombre ", nEntier ," est positif")
    elif nEntier == 0 :
        print("Le nombre ",nEntier," est nul")
    elif nEntier < 0 :
        print("Le nombre ",nEntier," est négatif")
    else :
        print("Une erreur est survenu")

# Procédure main()
def main():
    nEntier = int(input("Entrez un nombre entier :"))
    positifOuNegatif(nEntier)
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

