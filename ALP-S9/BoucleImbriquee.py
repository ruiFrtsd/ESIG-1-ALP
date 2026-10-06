# Boucle imbriquée
# Clément Vogt

# Problème: On aimerait savoir si les éléments d'une liste sont présents dans une autre liste.

# Procédures et fonctions
def afficher_liste(liste):
    for element in liste:
        print(element,end=' ')
    print()
    
def existe(un_composant,liste):
    for composant in liste:
        if composant == un_composant:
            return True
    return False

# Procédure main()
def main():
    lst1 = [8,4,22,17,7,20]
    lst2 = [2,8,11,12,20,44]
    
    print("lst1 = ",end='')
    afficher_liste(lst1)
    print("lst2 = ",end='')
    afficher_liste(lst2)
    
    
    # Version 1 : Il n'y a pas de boucles imbriquées car nous avons décomposé notre code! Utilisation d'une fonction existe() => BONNE PRATIQUE
    cpt = 0
    for composant in lst1:
        if existe(composant,lst2):
            print(cpt," ",composant," est dans les 2 listes ",sep='')
        cpt+=1
          
# Appel de la procédure main()
if __name__ == "__main__":
    main()