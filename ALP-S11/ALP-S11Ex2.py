# Imports

# Constantes
MINUSCULES = "abcdefghijklmnopqrstuvwxyz"
MAJUSCULES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM = "0123456789"

# Procédures et fonctions
def compte_et_affiche_types_de_car(tarte):
    cpt_minus,cpt_majus,cpt_num,cpt_autre = 0,0,0,0
    
    for lettre in tarte:
        for minus in MINUSCULES:
            if minus == lettre:
                cpt_minus +=1
        for majus in MAJUSCULES:
            if majus == lettre:
                cpt_majus +=1
        for num in NUM:
            if num == lettre:
                cpt_num += 1
        cpt_autre +=1
    
    cpt_autre = cpt_autre-cpt_majus-cpt_minus-cpt_num
    
    print(f"La chaîne contient {cpt_minus} minuscules, {cpt_majus} majuscule, {cpt_num} chiffres et {cpt_autre} autres symboles.")
# Procédure main()
def main():
    compte_et_affiche_types_de_car("P@#yn26at^&i5ve")
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
