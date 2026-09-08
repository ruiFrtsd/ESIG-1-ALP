# Imports

# Constantes
SEUIL_5 = 5
SEUIL_9 = 9
PRIX_DEBOUT = 20
PRIX_ASSISES = 30
# Procédures et fonctions
def entree():
    haut_ou_bas = int(input("Quel type de place souhaitez vous ? [1 => place debout, 2 => place assise]"))
    if haut_ou_bas == 1:
        place_debout = int(input("Combien de place debout :"))
    else:
        place_assises = int(input("Combien de place assises :"))
    
    return place_debout,place_assises,

def calculer(place_debout,place_assises):
    prix_final_debout = 0
    prix_final_assises = 0
    if place_debout >= SEUIL_9:
        place_debout -= 2
    elif place_debout >=SEUIL_5:
        place_debout -= 1
    
    if place_assises >= SEUIL_9:
        place_assises -= 2
    elif place_assises >= SEUIL_5:
        place_assises -= 1
        
        
        #ne prend pas encompte toute la valeur
    for i in range(place_assises):
        prix_final_assises += PRIX_ASSISES
    for i in range(place_debout):
        prix_final_debout += PRIX_DEBOUT
    
    return prix_final_debout,prix_final_assises

def afficher(place_debout,place_assises,prix_final_debout,prix_final_assises):
    print(f"Le prix à payer pour {place_debout} places debout : {prix_final_debout} Frs")
    print(f"Le prix à payer pour {place_assises} places assises : {prix_final_assises} Frs")
# Procédure main()
def main():
    place_debout,place_assises = entree()
    prix_final_debout,prix_final_assises = calculer(place_debout,place_assises)
    afficher(place_debout,place_assises,prix_final_debout,prix_final_assises)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
