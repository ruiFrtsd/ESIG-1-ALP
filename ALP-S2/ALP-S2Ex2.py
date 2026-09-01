# Imports

# Constantes
ANNEE_COURANTE = 2020 #annee en cours

PRIME_0 = 0 #prime pour ceux avec moins de 5 ans
PRIME_3 = 3 #prime pour ceux entre 5 et 10 ans
PRIME_7 = 7 #prime pour ceux avec plus de 10 ans

# Procédures et fonctions
#input user et affichage user
def entreeUtilisateur():
    salaireBase = float(input("Entrez le salaire de base : "))
    anneeEngagement = int(input("Entrez l'année d'engagement : "))
    anneeTravail = ANNEE_COURANTE - anneeEngagement
    retourCalculUtilisateur(salaireBase,anneeTravail)

def retourCalculUtilisateur(salaireBase,anneeTravail):
    print("Salaire de base :", salaireBase)
    print("Nombre d'année(s) :", anneeTravail, "an(s)")
    print("Prime : ",calculPrimeParSalaire(salaireBase,calculPrimeParAnDeTravail(anneeTravail)))
    print("salaire brut :", calculSalaireBrut(salaireBase,calculPrimeParAnDeTravail(anneeTravail)))

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
        entreeUtilisateur()

def calculPrimeParSalaire(salaireBase,prime):
    return calculSalaireBrut(salaireBase,prime) - salaireBase

def calculSalaireBrut(salaireBase,prime):
    salaireBrutPostPrime = (salaireBase*(prime/100))+salaireBase
    return salaireBrutPostPrime

# Procédure main()
def main():
    entreeUtilisateur()
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
