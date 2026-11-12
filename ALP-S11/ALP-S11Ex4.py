# Imports

# Constantes

# Procédures et fonctions
def estCePalindrome(mot):
    fah = ""
    
    for i in range(len(mot)-1, -1, -1):
        fah += mot[i]
    
    if fah == mot :
        return True 
    else :
        return False 
    
# Procédure main()
def main():
    motIn = input("quel mot ?")
    
    
    if estCePalindrome(motIn) :
        print(f"Le mot {motIn} est un palindrome")
    else :
        print(f"Le mot {motIn} n'est pas un palindrome")
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
