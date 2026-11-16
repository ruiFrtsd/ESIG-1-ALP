# Imports

# Constantes
TAHLESPACE = " "

# Procédures et fonctions
def escalierDescendant(mot):
    for i in range(0, len(mot), 1):
        print(TAHLESPACE*i, mot[i])
    

def escalierMontant(mot):
    n = len(mot)
    for i in range(n):
        nb_espaces = (n - 1) - i
        print(TAHLESPACE * nb_espaces, mot[i])

# Procédure main()
def main():
    escalierDescendant("abracadabra")
    escalierMontant("abracadabra")
# Appel de la procédure main()
if __name__ == "__main__":
    main()
