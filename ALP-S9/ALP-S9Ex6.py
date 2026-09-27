# Imports

# Constantes
NOTES = [3, 6, 5.5, 4.5, 2.5, 4, 5, 4, 3, 4, 2.5, 4.5, 5, 5, 4, 3]

# Procédures et fonctions
def moyennne_arrondie_deci_supp(liste):
    if liste:
        addition = 0
        compteur = 0
        for element_dans_liste in liste:
            addition += element_dans_liste
            compteur += 1
        
        x = round((addition / compteur),1)
        print("moyenne arrondie : ", x)
    else:
        print("liste vide")


def nombre_note_sous_4(liste):
    if liste:
        compteur = 0
        for element_dans_liste in liste:
            if element_dans_liste < 4.0:
                compteur += 1
        print("notes sous 4.0 : ", compteur)
    else:
        print("liste vide")
        
def meilleur_note(liste):
    if liste:
        meilleur = 0
        for element_dans_liste in liste:
            if element_dans_liste > meilleur:
                meilleur = element_dans_liste
        print("meilleur note : ", meilleur)
    else:
        print("liste vide")

def numero_ordre(liste):
    return None # j'ai pas compris
# Procédure main()
def main():
    moyennne_arrondie_deci_supp(NOTES)
    nombre_note_sous_4(NOTES)
    meilleur_note(NOTES)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()




