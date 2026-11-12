# Nom, prénom: MOTA Rui

# Imports

# Constantes
TERRAIN_ACCIDENTE = 1.20
TERRAIN_MONTAGNE = 1.50

DIFF_DENIVELE_TYPE1 = 200
DIFF_DENIVELE_TYPE2 = 150
DIFF_DENIVELE_TYPE3 = 100

RANDO_DEBUTANT_MOINS_10K = 2
RANDO_DEBUTANT_PLUS_10K = 5

SEUIL_FACILE = 10
SEUIL_MOYEN = 25
SEUIL_DIFFICILE = 35
# Procédures et fonctions
def vericationEntree(distance,denivele,terrain,niveau):
    erreur = True
    
    if distance < 0.0: # MS: <=
        print("La distance doit être supérieure à 0.")
        erreur = False
    if denivele <= 0: # MS: <
        print("Le dénivelé doit être positif ou nul.")
        erreur = False
    if terrain != 1 and terrain !=2 and terrain != 3 :
        print("Le type de terrain doit être 1, 2 ou 3.")
        erreur = False
    if niveau != 1 and niveau != 2 :
        print("Le niveau du randonneur doit être 1 ou 2.")
        erreur = False
    
    return erreur

def calcul(distance,denivele,terrain,niveau):
    indice = 0
    diff = 0
    coef = 1.0
    
    if terrain == 3 :
        diff = DIFF_DENIVELE_TYPE3
        coef = TERRAIN_MONTAGNE
    if terrain == 2 :
        diff = DIFF_DENIVELE_TYPE2
        coef = TERRAIN_ACCIDENTE
    if terrain == 1 :
        diff = DIFF_DENIVELE_TYPE1
    # MS: très bonne décomposition!
    indice = distance * coef + denivele / diff
    
    if niveau == 1: #if debutant
        if distance < 10 : # MS: bien, l'imbrication évite de retester le niveau
            indice += RANDO_DEBUTANT_MOINS_10K
        else :
            indice += RANDO_DEBUTANT_PLUS_10K
    
    return round(indice,1)

def determination_difficulte(indice):
    difficulte =""; # MS: c'est pas du C# :-)
    
    if indice < SEUIL_FACILE:
        difficulte =  "facile"
    if indice >= SEUIL_FACILE and indice < SEUIL_MOYEN: # MS: elif permettre d'éviter la redondance
        difficulte =  "moyenne"
    if indice >= SEUIL_MOYEN and indice < SEUIL_DIFFICILE:
        difficulte =  "difficile"
    if indice >= SEUIL_DIFFICILE:
        difficulte = "très difficile"
    
    return difficulte

def afficher(indice,difficulte):
    print(f"Indice final {indice} équivaut à : {difficulte}")

# Procédure main()
def main():
    distance = float(input("Distance en km :"))
    denivele = int(input("Dénivelé positif en mètres :"))
    terrain = int(input("Type de terrain (1: facile, 2: accidenté ou 3: montagne) :"))
    niveau = int(input("Niveau du randonneur (1: débutant, 2: expérimenté) :"))
    print("--------")
    if vericationEntree(distance,denivele,terrain,niveau):
        indice = calcul(distance,denivele,terrain,niveau)
        difficulte = determination_difficulte(indice)        
        afficher(indice,difficulte)    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
