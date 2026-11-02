# Imports

# Constantes
TEXTE = "abracadabra"
# Procédures et fonctions


def check(texte):
    cpt = 0
    for e in texte:
        if e == "a":
            cpt += 1
    return cpt
# Procédure main()
def main():
    cpt = check(TEXTE)
    print(f"la lettre 'a' se trouve {cpt} fois dans '{TEXTE}'")
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
