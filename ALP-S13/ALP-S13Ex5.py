LST_PAYS = ["Suisse", "France", "Congo", "Monténégro", "Tunisie", "Grèce", "Albanie", "Soudan"]
LST_CAPITALES = ["Berne", "Paris", "Kinshasa", "Podgorica", "Tunis", "Athènes", "Tirana", "Khartoum"]

#1 à l'aide d'une fonction,
#crééz, puis retournez un dictionnaire
#contenant les pays (en clé) et leur capitale (en valeur)
def mergeDict(d_pays,d_capitales):
    d_pays_capitales = {}

    for pays in range(len(d_pays)):
        d_pays_capitales[d_pays[pays]] = d_capitales[pays]
        
    return d_pays_capitales   

#2 à l'aide d'une procédure, affichez le dictionnaire nouvellement créé avec le format suivant :
# Capitale de Congo : Kinshasa et ainsi de suite pour toutes les entrées du dictionnaire
def affichageEnbellit(d_pays_capitales):
    for pays in d_pays_capitales:
        print(f"Capital de {pays} : {d_pays_capitales[pays]}")
    
#2.1 afficher une valeur spécifique du dictionnaire
def affichageEnbellitRequest(d_pays_capitales,paysDemande):
    if paysDemande in d_pays_capitales:
        print(f"Capital de {paysDemande} : {d_pays_capitales[paysDemande]}")

#3 à l'aide d'une nouvelle fonction, crééz un dictionnaire qui a pour clé les capitales et pour valeur un boolean
#Le boolean sert à savoir si la capitale est actuellement sûre à visiter. Mettez True pour toutes les capitales sauf
#Kinshasa et Khartoum, qui doivent être à false
def estCeQueCestSafeDyAller(d_pays_capitales):
    d_capitales_safe = {}
    
    # On itère directement sur les clés du dictionnaire
    for pays in d_pays_capitales:
        capitale = d_pays_capitales[pays]
        
        if capitale == "Kinshasa" or capitale == "Khartoum":
            d_capitales_safe[pays] = False
        else:
            d_capitales_safe[pays] = True
            
    return d_capitales_safe

#4 A partir du dictionnaire créé à l'étape 3, créer une procédure qui affiche le message suivant :
# Sur les 8 capitales présentes, 2 présentent des risques pour les voyageurs.
def retourSafe(d_capitales_safe):
    cptUnsafe = 0
    
    for capitale in d_capitales_safe:
        if d_capitales_safe[capitale] == False:
            cptUnsafe+=1
    
    print(f"Sur les {len(d_capitales_safe)} capitales présentes, {cptUnsafe} présentent des risques pour les voyageurs.")
    
#5 challenge : comment faire pour vérifier si une capitale (valeur) se trouve dans le dictionnaire initial
def estCeDansListe(d_pays_capitales,capitalDemande):    
    for cap in d_pays_capitales:
        if d_pays_capitales[cap] == capitalDemande:
            return "c'était dans la liste init"
        else :
            return "de quoi tu me parle ?"
    
# Procédure main()
def main():
    print("etape 1")
    print("")
    d_pays_capitales = mergeDict(LST_PAYS,LST_CAPITALES)
    affichageEnbellit(d_pays_capitales)
    print("")
    print("etape 2 - recherche dans liste : ")
    print("")
    paysDemande = input("Quel pays souhaité vous la capital ? ")
    affichageEnbellitRequest(d_pays_capitales,paysDemande)
    print("")
    print("etape 3 - safe ou pas safe ? : ")
    print("")
    d_capitales_safe = estCeQueCestSafeDyAller(d_pays_capitales)
    print(estCeQueCestSafeDyAller(d_pays_capitales))
    print("")
    print("etape 4 -  affiche safe ou pas safe : ")
    print("")
    retourSafe(d_capitales_safe)
    print("")
    print("etape 5 - Bonus : ")
    print("")
    capitalDemande = input("Quel capital souhaité vous verifier si il est dans le dictionnaire initial ? ")
    print (estCeDansListe(d_pays_capitales,capitalDemande))
# Appel de la procédure main()
if __name__ == "__main__":
    main()