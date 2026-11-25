# Imports

# Constantes
NOTES = [
    [2,5,3,6],
    [4,4,4,4],
    [4,4,4,4],
    [4,4,4,4],
    [4,4,4,4],
    [3,4,5,6]
]

# Procédures et fonctions
def show_eleve(val):
    print(NOTES[val])
    moy,meilleur,pire = 0.0,0,999
    for c in range(0,len(NOTES[val])):
        moy += NOTES[val][c]
        if NOTES[val][c] > meilleur:
            meilleur = NOTES[val][c]
        if NOTES[val][c] < pire:
            pire = NOTES[val][c]
    moy = moy / len(NOTES[val])
    
    print(moy)
    print(meilleur)
    print(pire)

def show_eval(evaluation):
    show_eval_table = []
    
    for c in range(0,len(NOTES)):
        show_eval_table += [NOTES[c][evaluation]]
    print(show_eval_table)
    
    moy,meilleur,pire = 0.0,0,999
    
    for l in range(0,len(show_eval_table)):
        moy += show_eval_table[l]
        if show_eval_table[l] > meilleur:
            meilleur = show_eval_table[l]
        if show_eval_table[l] < pire:
            pire = show_eval_table[l]
        
    moy = moy / len(show_eval_table)
    print(moy)
    print(meilleur)
    print(pire)



# Procédure main()
def main():
    val = int(input(f"Quel eleve chercher vous ? (0 à {len(NOTES)-1})"))
    show_eleve(val)
    evaluation = int(input(f"Quel evaluation chercher vous ? (0 à {len(NOTES[0])-1})"))
    show_eval(evaluation)
# Appel de la procédure main()
if __name__ == "__main__":
    main()
