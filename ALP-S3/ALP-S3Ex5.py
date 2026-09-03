# Imports

# Constantes
RABAIS_50P = 0.03
RABAIS_100P = 0.05
RABAIS_1000P = 0.10

TVA_MOINS_250P = 1.082
TVA_MOINS_500P = 1.063
TVA_PLUS_500P = 1.045
# Procédures et fonctions
def entree():
    nombre_piece = int(input("Entrez le nombre de pièce : "))
    prix_piece = int(input("Entrez le prix par pièce : "))
    
    return nombre_piece, prix_piece

def calculer_prix(nombre_piece, prix_piece):
    if nombre_piece >= 1000 :
        rabais = RABAIS_1000P 
    elif nombre_piece > 100 :
        rabais = RABAIS_100P
    else :
        rabais = RABAIS_50P
    if nombre_piece > 500 :
        tva = TVA_PLUS_500P
    elif nombre_piece > 250 :
        tva = TVA_MOINS_500P
    else :
        tva = TVA_MOINS_250P
        
    prix_post_modif = (nombre_piece*prix_piece)*(1-rabais)*tva    
    
    return rabais, tva,prix_post_modif

def afficher(nombre_piece, prix_piece,rabais, tva, prix_post_modif):
    print(f"Pour {nombre_piece} au prix unitaire de {prix_piece} et avec une reduction de {rabais*100}% et en prenant en compte la tva de {tva*100-100} le prix final sera de {prix_post_modif}")
# Procédure main()
def main():
    nombre_piece, prix_piece = entree()
    rabais, tva, prix_post_modif = calculer_prix(nombre_piece, prix_piece)
    afficher(nombre_piece, prix_piece,rabais, tva, prix_post_modif)
# Appel de la procédure main()
if __name__ == "__main__":
    main()

