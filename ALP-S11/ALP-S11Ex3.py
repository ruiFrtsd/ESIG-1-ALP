# Imports

# Constantes

# Procédures et fonctions
def ajoute_au_milieu(textOutside,textBetween):
    mid = len(textOutside) // 2
    # // utiliser afin d'avoir une valeur en int et non float lors d'une division normale
    out = textOutside[:mid] + textBetween + textOutside[mid:]    
    print(out)    
# Procédure main()
def main():
    ajoute_au_milieu("python", "COUCOU")
    ajoute_au_milieu("sandbox", "COUCOU")
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
