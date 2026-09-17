# Imports

# Constantes

# Procédures et fonctions
def entree():
    k = int(input("Entrez le nombre d'iteration "))
    n = int(input("Entrez la table de multiplication souhaitée "))
    
    return k,n

def affichage(k,n):
    for i in range(1,k+1):
        print(f"{i} x {n} = ", end="")
        print(i*n)
    
# Procédure main()
def main():
    k,n = entree()
    affichage(k,n)

# Appel de la procédure main()
if __name__ == "__main__":
    main()

