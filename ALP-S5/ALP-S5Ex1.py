# Imports

# Constantes
MSG_ERREUR = "Une erreur est survenue"


# Procédures et fonctions
def entree():
    type_piano = int(input("Entrez le type de votre piano (1 ou 2) : "))
    nombre_kilometre = int(input("Entrez le nombre de KM : "))
    nombre_etage_montes = int(input("Entrez le nombre d'étage montés : "))
    nombre_etage_decendus = int(input("Entrez le nombre d'étage decendus : "))
    
    return type_piano,nombre_kilometre,nombre_etage_montes,nombre_etage_decendus

#
# WIP
#

# Procédure main()
def main():
    type_piano,nombre_kilometre,nombre_etage_montes,nombre_etage_decendus = entree()
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

