# Imports

# Constantes
RABAIS = 0.1
QUANTITE_PASS = 100
# Procédures et fonctions
def entree():
    prix_unit = int(input("Entrez prix unitaire : "))
    quantite_unit = int(input("Entrez nombres de pièce(s) : "))
    prix_avant_rabais = prix_unit*quantite_unit
    return prixUnit,quantiteUnit,prix_avant_rabais

def calculer_rabais(quantite_unit, prix_avant_rabais):
    if quantite_unit <= QUANTITE_PASS :
        taux = 0
    else :
        taux = prix_avant_rabais * RABAIS
    return taux        

def caca():
    print("caca")
def afficher(taux)
    print("Le prix pour ", quantite_unit, "est :")
    print("prix avant rabais : ", prixUnit*quantiteUnit)
    print("montant du rabais : ", taux)
    print("prix à payer : ", prix_avant_rabais-rabais)

# Procédure main()
def main():
    entre
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

