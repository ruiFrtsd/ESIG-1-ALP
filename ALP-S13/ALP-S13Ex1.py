# Imports

# Constantes

# Procédures et fonctions

# Procédure main()
def main():

    # Initialisation du dictionnaire
    d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

    # 1. Corriger l'erreur dans le prénom
    d['prenom'] = 'Jacques'

    # --- Affichage des résultats ---

    # 2. Afficher la liste des clés
    print("--- Clés avec keys() ---")
    for cle in d.keys():
        print(cle)

    print("\n--- Clés sans keys() ---")
    for cle in d:
        print(cle)

    # 3. Afficher la liste des valeurs
    print("\n--- Valeurs avec values() ---")
    for valeur in d.values():
        print(valeur)

    print("\n--- Valeurs sans values() ---")
    for cle in d:
        print(d[cle])

    # 4. Afficher la liste des paires clé/valeur
    print("\n--- Paires avec items() ---")
    for cle, valeur in d.items():
        print(f"{cle} : {valeur}")

    print("\n--- Paires sans items() ---")
    for cle in d:
        print(f"{cle} : {d[cle]}")

    # 5. Ecrire la phrase finale
    print("\n--- Phrase finale ---")
    print(f"{d['prenom']} {d['nom']} a {d['age']} ans")
    
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
