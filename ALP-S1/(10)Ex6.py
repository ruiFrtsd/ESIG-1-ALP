salaireBase = int(input("Entrez le salaire de base : "))
anneeEngagement = int(input("Entrez l'année d'engagement : "))
prime = 0.0
if  (2020 - anneeEngagement) >= 5 :
    prime += 3.0

print("Salaire de base :", salaireBase)
print("Annee d'engagement", anneeEngagement)
print("nombre d'annee d'engagement", 2020-anneeEngagement, "ans" )
print("prime :", prime)
print("salaire", salaireBase*((100+prime)/100))