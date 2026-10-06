# Série 9, Exercice supplémentaire
# Clément Vogt

# Procédures et fonctions
# Procédure permettant d'afficher les valeurs contenues dans la liste reçue en paramètre. (Les éléments doivent être affichés les uns à côté des autres avec un espace entre chacun)
def afficher_liste_int(liste):
    for element in liste:
        print(element,end=' ')
    
# Fonction à résulat entier permettant de calculer et retourner la somme des valeurs int contenues dans la liste reçue en paramètre. 
def somme_liste_int(liste):
    somme = 0
    for element in liste:
        somme = somme + element       
    return somme

# Fonction à résultat booléean retournant True si et seulement si la liste reçue en paramètre contient au moins une valeur négative, False sinon.
def existe_valeur_negative_version_0(liste):
    negatif = False
    for element in liste:
        if element < 0:
            negatif = True       
    return negatif

# Fonction à résultat booléean retournant True si et seulement si la liste reçue en paramètre contient au moins une valeur négative, False sinon.
def existe_valeur_negative(liste):
    for element in liste:
        if element < 0:
            return True         
    return False
    # Avantage: quitte dès qu'on arrive sur une valeur négative

# !!! ATTENTION ERREUR COURANTE !!!
def existe_valeur_negative_faux(liste):
    for element in liste:
        if element < 0:   # Retourne True si négatif et False si positif, donc ne teste que la 1ère cellule ! 
            return True   # Donc retourne False si la 1ère cellule est positive sans regarder les cellules suivantes ! 
        else:             # Cette implémentation est donc INCORRECTE!!!
            return False

# Procédure main()
# Test des procédures à développer. Ne doit (en principe) pas être modifiée.
def main():
    lst1 = [1, 2, 3, 4, 5, 6, 7]
    lst2 = [1, 2, 7, -1, -2, -7, 0]
    
    print("Liste lst1: ",end='')
    afficher_liste_int(lst1)
    print()
    print("Liste lst2: ",end='')
    afficher_liste_int(lst2)
    print()
    print("Somme des valeurs de lst1: ", somme_liste_int(lst1),sep='')
    print("Somme des valeurs de lst2: ", somme_liste_int(lst2),sep='')
    if existe_valeur_negative(lst1):
        print("Il y a au moins une valeur négative dans lst1")
    if existe_valeur_negative(lst2):
        print("Il y a au moins une valeur négative dans lst2")

# Appel de la procédure main()
if __name__ == "__main__":
    main()