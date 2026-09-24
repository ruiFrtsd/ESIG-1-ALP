# Imports

# Constantes

# Procédures et fonctions
def entree():
    return int(input("Entrez une valeur N "))

def is_valid(n):
    valide = True
    if n <=0 :
        valide = False 
    
    return valide

def afficher(i, fn):
    print(f'F({i}) = {fn}')
    
# Procédure main()
def main():
    n = entree()   
    if is_valid(n):
        f0 = 0
        f1 = 1
        fn = 0 
        afficher(0,f0)
        afficher(1,f1)
        i=2
        while n > fn:
            fn = f0 + f1
            if fn < n :
                afficher(i, fn)
            f0 = f1
            f1 = fn
            i+=1
if __name__ == "__main__":
    main()






