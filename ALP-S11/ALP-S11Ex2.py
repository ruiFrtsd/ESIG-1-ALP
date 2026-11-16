# Imports

# Constantes
MINUSCULES = "abcdefghijklmnopqrstuvwxyz"
MAJUSCULES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM = "0123456789"

# Procédures et fonctions
def compte_et_affiche_types_de_car(tarte):
    cpt_minus,cpt_majus,cpt_num,cpt_autre = 0,0,0,0
    
    for lettre in tarte:
        if en(lettre, MAJUSCULES):
            cpt_majus +=1
        elif en(lettre,MINUSCULES):
            cpt_minus +=1
        elif en(lettre,NUM):
            cpt_num +=1
        else :
            cpt_autre +=1
            
    
    print(f"La chaîne contient {cpt_minus} minuscules, {cpt_majus} majuscule, {cpt_num} chiffres et {cpt_autre} autres symboles.")

def en(char,chaine):
    for i in range(len(chaine)):
        if char == chaine[i]:
            return True
    return False 

# Procédure main()
def main():
    compte_et_affiche_types_de_car("P@#yn26at^&i5ve")
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
