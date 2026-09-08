# Imports

# Constantes
TARIF_PIANO_DROIT = 60 
TARIF_PIANO_A_QUEUE = 90

TARIF_KM = 6
# Procédures et fonctions
def entree():
    type_piano = int(input("Quel est le type de piano [Piano droit -> 1 ou Piano à queue -> 2]"))
    nombre_etage_monter = int(input("Quel est le nombre d'étage à monter"))
    nombre_etage_descendre = int(input("Quel est le nombre d'étage à descendre"))
    nombre_km = int(input("Quel est le nombre de kilometres à éffectuer"))
    
    return type_piano,nombre_etage_monter,nombre_etage_descendre,nombre_km

def calculer(type_piano,nombre_etage_monter,nombre_etage_descendre,nombre_km):
   tarif_total_km = 0
   tarif_total_etage = 0
   
   if type_piano == 1: #piano droit
        tarif_piano = TARIF_PIANO_DROIT
   elif type_piano == 2: #piano a queue
        tarif_piano = TARIF_PIANO_A_QUEUE
   else:
        print("erreur")
    
   if (nombre_etage_descendre+nombre_etage_monter) > 10:
       tarif_total_etage = tarif_piano * 10
   else:
       for eta in range(nombre_etage_descendre+nombre_etage_monter):
           tarif_total_etage += tarif_piano
    
   for i in range(nombre_km):
        tarif_total_km += TARIF_KM
        
   tarif_final = tarif_total_etage+tarif_total_km
   
   if tarif_final < 200:
       tarif_final = 200
   elif tarif_final >2500:
       tarif_final = 2500
        
   return tarif_final,tarif_total_km

def afficher(type_piano,tarif_total_km,nombre_km,tarif_final):
    if type_piano == 1:
        print(f"Prix total à payer pour un piano :{tarif_final}.- (dont {tarif_total_km}.- de transport pour les {nombre_km}km)")
    elif type_piano == 2:
        print(f"Prix total à payer pour un piano à queue :{tarif_final}.- (dont {tarif_total_km}.- de transport pour les {nombre_km}km)")
    
# Procédure main()
def main():
    type_piano,nombre_etage_monter,nombre_etage_descendre,nombre_km = entree()
    tarif_final, tarif_total_km = calculer(type_piano,nombre_etage_monter,nombre_etage_descendre,nombre_km)
    afficher(type_piano,tarif_total_km,nombre_km,tarif_final)
# Appel de la procédure main()
if __name__ == "__main__":
    main()

