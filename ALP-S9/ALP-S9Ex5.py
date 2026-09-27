# Imports

# Constantes

RELEVES = [11.8, 14.4, 18.6, 16.5, 11.5, 12.3, 9.1]

# Procédures et fonctions
def temp_moyenne(liste):
    if liste:
        addition = 0
        division = 0
        for element_dans_liste in liste:
            addition += element_dans_liste
            division += 1
        moyenne = addition/division
        print("moyenne est : ")
        print(moyenne)
    else:
        print('La liste fournie est vide')
        
def nombre_temp_sous_15(liste):
    if liste:
        compteur_temp_sous_15 = 0
        for element_dans_liste in liste:
            if element_dans_liste < 15:
                compteur_temp_sous_15 +=1
        print("nombre de temperature sous 15 degres :")
        print(compteur_temp_sous_15)
        
    else:
        print('La liste fournie est vide')
# Procédure main()
def main():
    temp_moyenne(RELEVES)
    nombre_temp_sous_15(RELEVES)
# Appel de la procédure main()
if __name__ == "__main__":
    main()



