# Imports

# Constantes

L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8] #liste de 10 nombres entiers

# Procédures et fonctions
def nombre_elements_entre(liste,borne_min,borne_max):
    if liste:
        compteur_elements_entre = 0
        for element_dans_liste in liste:
            if element_dans_liste > borne_min and element_dans_liste < borne_max:
                compteur_elements_entre +=1
                
        print(f"Nombres d'élements entre les 2 bornes est : { compteur_elements_entre }.")
    else:
        print('La liste fournie est vide') 
# Procédure main()
def main():
    nombre_elements_entre(L10_INT,5,5)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()


