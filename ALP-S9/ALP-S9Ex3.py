# Imports

# Constantes

L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

L2_STR = ["alice", "bob"] #liste de deux chaînes de caractères 

L1_FLO = [-3.5,2.5] #liste de un seul nombre réel 

L0 = [] #liste vide

# Procédures et fonctions
def afficher_positif(liste):
    if liste:
        for element_dans_liste in liste:
            if element_dans_liste >= 0:
                print(element_dans_liste)
    else:
        print('La liste fournie est vide') 
# Procédure main()
def main():
    afficher_positif(L10_INT)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

