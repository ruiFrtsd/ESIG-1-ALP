# Imports

# Constantes

# Procédures et fonctions
def max_xp(dico):
    max_plongee = -1
    le_meilleur = ""
    
    for nom in dico:
        meilleur_actuel = dico[nom]
        if meilleur_actuel > max_plongee:
            max_plongee = meilleur_actuel
            le_meilleur = nom
            
    
    output = {}
    output['nom'] = le_meilleur
    output['plongees'] = max_plongee
    
    return output
    
# Procédure main()
def main():
    NOMS = ['Londa','Lenita','Beatrice','Kendrick','Genny','Rolf','Meridith','Hilton','Phylis','Candis','Ron','Lecia','Jacquelyn','Gonzalo','Herlinda','Morgan','Han','Sanjuanita','Allie','Fernande','Anna','Gracia','Lula','Merlyn','Tandy','Adah','Ozella','Laureen','Ricky','Miki']
    NB_PLONGEES = [20,120,15,150,5,20,30,60,100,8,20,15,30,79,130,66,24,110,8,23,20,77,60,22,30,80,50,20,10,29]
    
    d_plongees = {}
    #fusioner 2 dictionaire dans un dictionnaire
    for nom in range(len(NOMS)):
        d_plongees[NOMS[nom]] = NB_PLONGEES[nom]

    print(d_plongees)
    
    print()
    #rechercher un element dans le dict
    lookHerUp = input("qui voulez vous rechercher ? ")
    
    for nom in d_plongees:
        if nom == lookHerUp:
            print("nb de plongee", d_plongees[nom])
            
    print(max_xp(d_plongees))
# Appel de la procédure main()
if __name__ == "__main__":
    main()
