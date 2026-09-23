# Imports

# Constantes

L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

L2_STR = ["alice", "bob"] #liste de deux chaînes de caractères 

L1_FLO = [-3.5,2.5] #liste de un seul nombre réel 

L0 = [] #liste vide

# Procédures et fonctions
def premier_de_la_liste(liste):
    print(liste[0])
    
def dernier_de_la_liste(liste):
    print(liste[-1])
    
def avant_dernier_de_la_liste(liste):
    print(liste[-2])
    
def nieme_valeur_de_la_liste(liste,n):
    if n < liste[-1] :
        print(liste[n])
    else :
        print('N/A')

# Procédure main()
def main():
    avant_dernier_de_la_liste(L0)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()

