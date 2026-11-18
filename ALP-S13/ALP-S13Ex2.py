# Imports

# Constantes

# Procédures et fonctions

# Procédure main()
def main():
    prix = {"bananes": 4, "pommes": 2, "oranges": 1.5, "poires": 3}
    stock = {"bananes": 100, "pommes": 290, "oranges": 50, "poires": 120}
    
    for valeur_recherchee in prix:
        valeur_calculer= prix[valeur_recherchee] * stock[valeur_recherchee]
        print(f"{valeur_recherchee} : {valeur_calculer} CHf")
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
