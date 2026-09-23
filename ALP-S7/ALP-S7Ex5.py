# Imports

# Constantes

# Procédures et fonctions
def entree():
    n = int(input("Entrez valeur N "))
    
    return n
def calculer(n):
    y=1
    for i in range (1, n+1, 1):
        print(f"{y} x {i} = {y*i}")
        y *= i
        

# Procédure main()
def main():
    n = entree()
    calculer(n)
# Appel de la procédure main()
if __name__ == "__main__":
    main()




