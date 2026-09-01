# Imports

# Constantes
ANNEE_COURANTE = 2020 #annee en cours

PRIME_0 = 0.0  #prime pour ceux avec moins de 5 ans
PRIME_3 = 0.03 #prime pour ceux entre 5 et 10 ans
PRIME_7 = 0.07 #prime pour ceux avec plus de 10 ans

# Procédures et fonctions
#input user et affichage user
def entreeUtilisateur():
    salaireBase = float(input("Entrez le salaire de base : "))
    anneeEngagement = int(input("Entrez l'année d'engagement : "))
    return salaireBase, anneeEngagement


def afficher(salaireBase,anneeTravail, montant_prime, salaire_brut):
    print("Salaire de base :", salaireBase)
    print("Nombre d'année(s) :", anneeTravail, "an(s)")
    print("Prime : ", montant_prime)
    print("salaire brut :", salaire_brut)

#calcul logique
def calculPrimeParAnDeTravail(anneeTravail):
    if anneeTravail < 5:
        return PRIME_0
    elif anneeTravail >= 5 and anneeTravail <=10 :
        return PRIME_3
    elif anneeTravail > 10 :
        return PRIME_7
    else :
        print("une erreur est survenu")
        # entreeUtilisateur()

def calculPrimeParSalaire(salaire_brut,salaire_base):
    return salaire_brut - salaire_base

def calculSalaireBrut(salaireBase,prime):
    salaireBrutPostPrime = (salaireBase*prime)+salaireBase
    return salaireBrutPostPrime

# Procédure main()
def main():
    # 1. Acquisition des données
    salaire_base, annee_engagement = entreeUtilisateur()
    
    # 2. Traitement
    anneeTravail = ANNEE_COURANTE - annee_engagement
    salaire_brut = calculSalaireBrut(salaire_base,calculPrimeParAnDeTravail(anneeTravail))
    montant_prime = calculPrimeParSalaire(salaire_brut, salaire_base)

    # 3. Restitution / Affichage
    afficher(salaire_base,anneeTravail, montant_prime, salaire_brut)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
