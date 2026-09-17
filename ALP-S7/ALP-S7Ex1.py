# Imports

# Constantes

# Procédures et fonctions
def entree():
    n = int(input("entrez un nombre "))
    
    return n

def affichage(n):
    for i in range(0,n+1,1):
        if i % 2 == 0:
            print(i)
    
# Procédure main()
def main():
    n = entree()
    affichage(n)

# Appel de la procédure main()
if __name__ == "__main__":
    main()


