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
        tva = TVA_PLUS_500P
    elif nombre_piece > 500 :
# Procédure main()
def main():
    nombre_piece, prix_piece = entree()
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

