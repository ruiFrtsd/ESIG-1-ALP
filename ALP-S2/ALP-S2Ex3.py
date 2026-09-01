# Imports

# Constantes
RABAIS_TYPE_1 = 0.2
RABAIS_TYPE_2 = 0.1
RABAIS_TYPE_3 = 0.0

RABAIS_VOLS_1 = 0.10
RABAIS_VOLS_2 = 0.15
RABAIS_VOLS_3 = 0.20
# Procédures et fonctions
#entree et affichage utilisateur
def recuperer_valeurs_utilisateur():
    prix = int(input("Entrez un prix initial : "))
    type_utilisateur = int(input("Entrez un type voyageur : "))
    nombre_vol = int(input("Entrez un nombre de vol : "))
    return prix, type_utilisateur,nombre_vol

def afficher():
#calcul
def categoriser_utilisateur_type(type_utilisateur):
    if type_utilisateur == 1 :
        return RABAIS_1
    elif type_utilisateur == 2 :
        return RABAIS_2
    elif type_utilisateur == 3 :
        return RABAIS_3
    else:
        print("une erreur est survenue")
        
def categoriser_utilisateur_nombre(nombre_vol):
    if nombre_vol == 1 :
        return RABAIS_1
    elif nombre_vol == 2 or 3 or 4 :
        return RABAIS_2
    elif nombre_vol >= 5 :
        return RABAIS_3
    else:
        return 0
    
def calculer_prix_vol():
# Procédure main()
def main():
    # 1. Acquisition des données
    prix,type_utilisateur,nombre_vol = recuperer_valeurs_utilisateur()
    # 2. Traitement
    rabais_type_disponible = categoriser_utilisateur_type(type_utilisateur)
    rabais_utilisateur_disponible = categoriser_utilisateur_type(nombre_vol)
    # 3. Restitution / Affichage
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

