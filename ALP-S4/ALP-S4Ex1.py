# Imports

# Constantes
TARIF_PIANO_DROIT = 60 
TARIF_PIANO_A_QUEUE = 90

TARIF_KM = 6
# Procédures et fonctions
def entree():
    type_piano = int(input("Quel est le type de piano [Piano droit -> 1 ou Piano à queue -> 2]"))
    nombre_etage_monter = int(input("Quel est le nombre d'étage à monter"))
    nombre_etage_descendre = int(input("Quel est le nombre d'étage à descendre"))
    nombre_km = int(input("Quel est le nombre de kilometres à éffectuer"))
    
    return type_piano,nombre_etage_monter,nombre_etage_descendre,nombre_km

def calculer(type_piano,nombre_etage_monter,nombre_etage_descendre,nombre_km):
   tarif_total_km = 0
   if type_piano == 1 : #piano droit
        tarif_piano = TARIF_PIANO_DROIT
    elif type_piano == 2:
        tarif_piano = TARIF_PIANO_A_QUEUE
    else :
        print("erreur")
    
    for i in range(nombre_km):
        tarif_total_km += TARIF_KM
        
    #
    # WIP
    #
# Procédure main()
def main():
    type_piano,nombre_etage_monter,nombre_etage_descendre,nombre_km = entree()
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

