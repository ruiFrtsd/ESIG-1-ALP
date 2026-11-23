# Imports

# Constantes
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
OBELIX = "*"
# Procédures et fonctions
    
# Procédure main()
def main():
    poids_de_caractere = {}
    
    for lettre in range(len(ALPHABET)):
        poids_de_caractere[ALPHABET[lettre]] = 0
    
    strToCheck = "Exo 10 : Le Premier Exemple"
    
    for char in strToCheck:
        if char in poids_de_caractere:
            poids_de_caractere[char] += 1
    
    for element in poids_de_caractere:
        print(f"{element}: {OBELIX*poids_de_caractere[element]} {poids_de_caractere[element]}")
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

