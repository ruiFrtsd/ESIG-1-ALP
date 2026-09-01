# Imports

# Constantes
RABAIS = 0.1
QUANTITE_PASS = 100
# Procédures et fonctions
def entree():
    prix_unit = float(input("Entrez prix unitaire : "))
    quantite_unit = int(input("Entrez nombres de pièce(s) : "))
    prix_avant_rabais = prix_unit*quantite_unit
    return prix_unit,quantite_unit,prix_avant_rabais

def calculer_rabais(quantite_unit, prix_avant_rabais):
    if quantite_unit <= QUANTITE_PASS :
        taux = 0
    else :
        taux = prix_avant_rabais * RABAIS
    return taux        

def afficher(prix_unit,quantite_unit,prix_avant_rabais,taux):
    print("Pour ", quantite_unit, " pièces à ",prix_unit ,":")
    print("prix avant rabais : ", prix_unit*quantite_unit)
    print("montant du rabais : ", taux)
    print("prix à payer : ", prix_avant_rabais-taux)

# Procédure main()
def main():
    prix_unit,quantite_unit,prix_avant_rabais = entree()
    taux = calculer_rabais(quantite_unit,prix_avant_rabais)
    afficher(prix_unit,quantite_unit,prix_avant_rabais,taux)
# Appel de la procédure main()
if __name__ == "__main__":
    main()

