# Imports

# Constantes

# Procédures et fonctions
def entree():
    n = int(input("entrez un petit nombre "))
    m = int(input("entrez un grand nombre "))
    
    if m<n:
        print("le deuxieme nombre etait plus petit que le premier \nVeuillez rerentrer des valeurs")
        return entree()        
    else:
        return n,m
def affichage(n,m):
    for i in range(n,m):
        print(i)
            
# Procédure main()
def main():
    n, m = entree()
    affichage(n,m+1)

# Appel de la procédure main()
if __name__ == "__main__":
    main()
