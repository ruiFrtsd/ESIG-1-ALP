# Constantes


# Procédures et fonctions
def afficher_premieres_durees(lst_durees, nb):
    pass
 
def calculer_duree_totale(lst_emprunts, lst_livres, lst_durees):
    pass


# Procédure main()
'''
Cette procédure permet de tester les 3 procédures ci-dessus :
elle commence par remplir les listes avant d'appeler vos 3 procédures. 

Vous n'avez pas le droit de modifier cette procédure.
'''
def main():
    lst_livres = ["Le Seigneur des anneaux", "Le Trône de fer", "L'Apprenti assassin", "Bilbo le Hobbit", "The Empyrean", "Le sorceleur"]
    lst_durees = [30, 0, 0, 80, 20, 7]
    lst_emprunts = ["The Empyrean", "Harry Potter", "Le Seigneur des anneaux","Un palais d'épines et de roses"]
    
    nb = int(input("Entrez un nombre de durées non-nulles à afficher (Partie A)"))
    
    print("Liste des durées de prêt :", lst_durees)

    print("\nPartie A")
    afficher_premieres_durees(lst_durees, nb)
    
    print("\nPartie B")
    calculer_duree_totale(lst_emprunts, lst_livres, lst_durees)


# Appel de la procédure main()
if __name__ == "__main__":
    main()
