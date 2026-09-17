# Imports

# Constantes

# Procédures et fonctions
def entree():
    capital = int(input("Entrez un capital de départ "))
    taux = int(input("Entrez un taux d'intérêt "))
    annee = int(input("Entrez un nombre de périodes (en annee) "))
    
    return capital,taux,annee
def calculer(capital,taux,annee):
    
    total = capital * (1+taux/100)**annee # le "**" est utiliser pour calculer une puissance
    return total

##faux faire avec une boucle for mdr

# Procédure main()
def main():
    capital,taux,annee = entree()
    print(calculer(capital,taux,annee))
# Appel de la procédure main()
if __name__ == "__main__":
    main()



