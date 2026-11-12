# Nom, prénom : 

# Imports

# Constantes
TEMPS = 15
DPLUS = 100
DMOINS = 200

# Procédures et fonctions

def duree(distance, montee, descente):
    duree_trajet = round((distance*TEMPS) + ((montee/DPLUS)*TEMPS) + ((descente/DMOINS)*TEMPS))
    return duree_trajet

def afficher_durees(titres, distances, montees, descentes):
    print("--- Durées à l'aller ---")
    totale_aller=0
    cpt_aller = 0
    for etape in range(len(titres)):
        duree_trajet = duree(distances[etape], montees[etape], descentes[etape])
        totale_aller += duree_trajet
        cpt_aller +=1
        print(f"Étape {etape+1} ({titres[etape]}) : {duree_trajet} min")
    print(f"Durée totale à l'aller : {totale_aller}")
    print(f"Durée moyenne des étapes à l'aller : {round(totale_aller/cpt_aller)}")
    print("--- Durées au retour ---")
    
    totale_retour = 0
    cpt_retour = 0
    for etape in range(len(titres),0,-1):
        duree_trajet = duree(distances[etape-1],descentes[etape-1] , montees[etape-1])
        totale_retour += duree_trajet
        cpt_retour +=1
        print(f"Étape {etape} ({titres[etape-1]}) : {duree_trajet} min")
    print(f"Durée totale à l'retour : {totale_retour}")
    print(f"Durée moyenne des étapes à l'aller : {round(totale_retour/cpt_retour)}")  # MS: "au retour ... min"
 
def afficher_plus_longue_descente(montees, descentes):#c'est des tableaux ca coute rien de l'indiqué
    print("--- Descente nette ---")
    longeur = 0
    index_min = 0
    index_max = 0
    for index in range(len(montees)):
        if montees[index] < descentes[index]: # MS: comparaison inversée, j'ai corrigée
            longeur +=1 # MS: c'est la bonne idée
            index_min = index
        index_max = index
    
    if longeur != 0:
        print(f"Plus longue suite d'étapes en descente nette : étapes {index_min} à {index_max} (longueur : {longeur})")
    else :
        print("Aucune étape en descente nette")

#  Procédure afficher_rapport - NE PAS MODIFIER
def afficher_rapport(nom, titres, distances, montees, descentes):
    print(f"===== {nom} =====")
    afficher_durees(titres, distances, montees, descentes)
    afficher_plus_longue_descente(montees, descentes)


# Procédure main() - NE PAS MODIFIER
def main():
    # Itinéraire A (données fictives)
    titres_a = ["Val-Fleuri – Alpe du Chamois", "Alpe du Chamois – Col des Marmottes",
                "Col des Marmottes – Lac Noir", "Lac Noir – Les Granges",
                "Les Granges – Pont du Diable", "Pont du Diable – Val-Fleuri"]
    distances_a = [8.2, 6.4, 9.4, 11.0, 7.8, 5.6]    # km
    montees_a = [640, 510, 110, 150, 100, 240]       # m
    descentes_a = [80, 60, 470, 630, 310, 200]       # m

    # Itinéraire B (données fictives)
    titres_b = ["Lac-sur-Rive – Les Vignes", "Les Vignes – Bois-Joli",
                "Bois-Joli – Alpage des Sources", "Alpage des Sources – Cabane du Glacier",
                "Cabane du Glacier – Col du Glacier"]
    distances_b = [9.0, 7.6, 16.2, 5.0, 4.4]         # km
    montees_b = [320, 410, 980, 600, 150]            # m
    descentes_b = [40, 20, 110, 0, 150]              # m

    # Itinéraire C (données fictives)
    titres_c = ["Cabane des Aigles – Alpe Rousse", "Alpe Rousse – Les Mayens",
                "Les Mayens – Chapelle Saint-Jean", "Chapelle Saint-Jean – Crête du Loup",
                "Crête du Loup – Les Planches", "Les Planches – Moulin-Neuf",
                "Moulin-Neuf – Port-Joli"]
    distances_c = [6.0, 7.2, 5.4, 8.0, 9.6, 6.4, 7.0]   # km
    montees_c = [70, 60, 250, 650, 90, 40, 20]          # m
    descentes_c = [420, 370, 250, 50, 230, 160, 90]     # m

    afficher_rapport("Tour du Val-Fleuri", titres_a, distances_a,
                     montees_a, descentes_a)
    print()
    afficher_rapport("Montée au Col du Glacier", titres_b, distances_b,
                     montees_b, descentes_b)
    print()
    afficher_rapport("Descente vers le lac", titres_c, distances_c,
                     montees_c, descentes_c)

# Appel de la procédure main()
if __name__ == "__main__":
    main()
