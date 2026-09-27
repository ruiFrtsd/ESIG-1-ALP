# Imports

# Constantes

L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

L2_STR = ["alice", "bob"] #liste de deux chaînes de caractères 

L1_FLO = [-3.5,2.5] #liste de un seul nombre réel 

L0 = [] #liste vide

# Procédures et fonctions
def premier_de_la_liste(liste):
    if liste:
        print(liste[0])
    else:
        print('La liste fournie est vide')
    
def dernier_de_la_liste(liste):
    if liste:
        print(liste[-1])
    else:
        print('La liste fournie est vide')
    
def avant_dernier_de_la_liste(liste):
    if liste:
        print(liste[-2])
    else:
        print('La liste fournie est vide')
    
def nieme_valeur_de_la_liste(liste,n):
    if liste:
        longeur_liste = 0
        for i in liste:
            longeur_liste +=1
    
        if n-1 < longeur_liste :
            print(liste[n-1])  # '-1' ajouter afin que la recherche soit faite avec la logique humaine 1 à X de la liste et non la logique 0 à X des machines
        else :
            print('N/A')
    else:
        print('La liste fournie est vide')
    
def afficher_liste(liste):
    if liste:
        for element_dans_liste in liste:
            print(element_dans_liste)
    else:
        print('La liste fournie est vide') 
# Procédure main()
def main():
    afficher_liste(L10_INT)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

