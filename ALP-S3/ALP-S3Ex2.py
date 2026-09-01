# Imports

# Constantes
RABAIS = 0.5
# Procédures et fonctions
def entree():
    numero_client = int(input("Entrez un numéro de client "))
    prix_article_1 = int(input("Entrez le prix du premier article "))
    prix_article_2 = int(input("Entrez le prix du deuxième article "))
    return numero_client, prix_article_1, prix_article_2
    

def calculer_ticket(prix_article_1, prix_article_2):
    if prix_article_1 > prix_article_2: #si le 2eme prix est plus petit que le premier alors sa valeur est diviser par 2
        prix_article_2 = prix_article_2*RABAIS
    elif prix_article_2 > prix_article_1:#si le 1er prix est plus petit que le deuxieme alors sa valeur est diviser par 2
        prix_article_1 = prix_article_1*RABAIS
    prix_a_payer = prix_article_1 + prix_article_2
    return prix_a_payer

def impression_ticket(numero_client, prix_article_1, prix_article_2,prix_a_payer):
    print("Magasin PTIPRI")
    print("Achats effectuées par le client n°",numero_client)
    print("Prix des 2 articles achetés : ", prix_article_1 ," et ", prix_article_2 , "==> Prix à payer:", prix_a_payer)
    print("""Merci pour votre achat
En cas de problème. vous pouvez nous les retourner dans les 7 jours.""")
    
# Procédure main()
def main():
    numero_client, prix_article_1, prix_article_2 = entree()
    prix_a_payer = float(calculer_ticket(prix_article_1, prix_article_2))
    impression_ticket(numero_client, prix_article_1, prix_article_2,prix_a_payer)
#Appel de la procédure main()
if __name__ == "__main__":
    main()

