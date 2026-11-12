# Imports

# Constantes
TAHLESPACE = " "
# Procédures et fonctions
def escalierDescendant(mot):
    for i in range(0, len(mot), 1):
        print(TAHLESPACE*i, mot[i])
    

def escalierMontant(mot):
    out,out2 = "",""
    for z in range(len(mot)):
        out += TAHLESPACE
    
    for i in range(len(mot)-1, 0 , -1):
        out2 = out.strip(TAHLESPACE)
        print(out, mot[i],i)
   

# Procédure main()
def main():
    escalierDescendant("abracadabra")
    escalierMontant("abracadabra")
# Appel de la procédure main()
if __name__ == "__main__":
    main()
