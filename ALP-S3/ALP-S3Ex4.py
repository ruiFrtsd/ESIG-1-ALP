# Imports

# Constantes
OUI_65 = 0.65
BONUS_MIN = 5000
BONUS_MED = 8000
BONUS_MAX = 12000
BONUS_MAJORITE = 2000
BONUS_POURCENTAGE = 4000
SEUIL_VOTE_1 = 1000
SEUIL_VOTE_2 = 2000

# Procédures et fonctions
def entree():
    oui_quantite= int(input("Nombre de oui"))
    non_quantite= int(input("Nombre de non"))
    
    return oui_quantite,non_quantite

def calculer_votation(oui_quantite,non_quantite):
    if (oui_quantite + non_quantite) > SEUIL_VOTE_2 :
        moula = BONUS_MAX
    elif (oui_quantite + non_quantite) > SEUIL_VOTE_1 :
        moula = BONUS_MED
    else :
        moula = BONUS_MIN
        
    if oui_quantite > non_quantite :
        moula += BONUS_MAJORITE
    
    if oui_quantite > OUI_65*(oui_quantite + non_quantite) :#si la quantité de oui est plus grande que 65% des vote totaux
        moula += BONUS_POURCENTAGE
        
    return moula

def affichage(oui_quantite,non_quantite,moula):
    print("Le montant pour cette commune ayant ",oui_quantite," OUI et ",non_quantite," NON sera de CHF ",moula,".-")
# Procédure main()
def main():
    oui_quantite,non_quantite = entree()
    moula = calculer_votation(oui_quantite,non_quantite)
    affichage(oui_quantite,non_quantite,moula)
#Appel de la procédure main()
if __name__ == "__main__":
    main()

