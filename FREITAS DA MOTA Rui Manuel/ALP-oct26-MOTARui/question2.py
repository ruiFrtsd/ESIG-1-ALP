# Nom, prénom: MOTA Rui

# Imports

# Constantes
RECOLTE_JOUR = 20 
# Procédures et fonctions
def calcul(objectif,participants_inscrits,nouveaux_participants,participants_sortants):
    # MS: la première partie de cette procédure est très propre, aspect pro !
    recolte,jour,sorti = 0,0,0
    participants = participants_inscrits
    while recolte < objectif:
        jour += 1
        if jour % 3 == 0:
            sorti += participants_sortants
            participants -= participants_sortants
        participants += nouveaux_participants
        recolte += participants * RECOLTE_JOUR
        
    if recolte == objectif:
        print("Objectif atteint !")
    if recolte > objectif: # MS: else?
        print("Objectif dépassé !")
        
    print(f"Nombre de jours : {jour}")
    print(f"Participants à la fin : {participants-participants_inscrits}")
    #  MS: Très bonne idée de déduire le nombre d'arrivée,
    #   bien qu'il manque -participants_inscrits, je compte juste
    print(f"Nombre total d'arrivées : {participants - sorti}")
    print(f"Nombre total de départs : {sorti}")
    print(f"Montant total récolté : {recolte} CHF")

# Procédure main()
def main():
    objectif = int(input("Objectif de dons en CHF :"))
    participants_inscrits = int(input("Participants initialement inscrits pour la randonnée :"))
    nouveaux_participants = int(input("Personnes rejoignant le groupe chaque jour :"))
    participants_sortants = int(input("Personnes quittant le groupe tous les 3 jours :"))
    print("--------")
    calcul(objectif,participants_inscrits,nouveaux_participants,participants_sortants)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
