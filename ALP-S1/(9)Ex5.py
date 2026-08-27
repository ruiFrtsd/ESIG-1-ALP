prixUnit = int(input("Entrez prix unitaire : "))
quantiteUnit = int(input("Entrez nombres de pièce(s) : "))
prixAvantRabais = prixUnit*quantiteUnit
rabais = 0

if quantiteUnit <= 100 :
    rabais = 0
else :
    rabais = prixAvantRabais * 0.1

print("Le prix pour ", quantiteUnit, "est :")
print("prix avant rabais : ", prixUnit*quantiteUnit)
print("montant du rabais : ", rabais)
print("prix à payer : ", prixAvantRabais-rabais)