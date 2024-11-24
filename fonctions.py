# Fonctionnalité 1 : Calcul de remise => menu.py choix 1
# Définition de la fonction (def) pour calculer une remise
def calcul_remise(_montant, _remise): 
    # Calcul du prix après remise
    resultat = _montant - _montant * (_remise/100)
    # Affichage du résultat
    return print("Le prix de l'article après la remise est de : " + str(resultat) + " €")

###################################################################################################
# Fonctionnalité 2 : Lancé de dés => menu.py choix 2
import random  # Importation du module random pour générer des nombres aléatoires
# Définition de la fonction (def) pour clancer le dé
def lance_des():
    """Cette fonction permet à l'utilisateur de lancer un dé avec un nombre de faces choisi."""
    
    while True:  # Boucle pour permettre à l'utilisateur de rejouer
        # Demande à l'utilisateur combien de faces doit avoir le dé
        faces = int(input("Entrez le nombre de faces du dé (minimum 4) : "))
        
        # Vérifie que le nombre de faces est valide
        if faces < 4:
            print("Veuillez entrer un nombre de faces supérieur ou égal à 4.")
            continue  # Redemande le nombre de faces si moins de 4
        
        # Lance le dé en générant un nombre aléatoire entre 1 et le nombre de faces
        resultat = random.randint(1, faces)
        
        # Affiche le résultat du lancer
        print(f"Vous avez lancé le dé : {resultat}")
        
        # Demande à l'utilisateur s'il veut relancer le dé
        rejouer = input("Voulez-vous lancer à nouveau ? (o/n) : ").lower()
        
        # Si l'utilisateur ne veut pas rejouer, on sort de la boucle
        if rejouer != 'o':
            return print("Le résultat du lancé est de : " + str(resultat) + "pour un dé à " + str(faces) + " faces")
            # Retourne le résultat final du lancer

# Exemple d'appel de la fonction (décommenter pour tester)
# dernier_resultat = lance_des()
# print(f"Le dernier résultat du dé était : {dernier_resultat}")

###################################################################################################
# Fonctionnalité 3 : Trouver le juste prix => menu.py choix 3

import random  # Importation du module random pour générer des nombres aléatoires

def juste_prix():
    """Cette fonction permet à l'utilisateur de deviner un prix entre 1 et 100 euros."""
    
    continuer = True  # Variable pour contrôler si le jeu continue
    
    while continuer:  # Boucle tant que continuer est vrai
        juste_prix = random.randint(1, 100)  # Générer un juste prix aléatoire
        essais = 0  # Compteur d'essais
        max_essais = 5  # Nombre maximum d'essais autorisés
        
        print("Bienvenue au jeu du juste prix !")  # Message d'accueil
        print("Devinez le prix entre 1 et 100 euros.")  # Instructions
        
        while essais < max_essais:  # Boucle pour les essais
            proposition = int(input("Entrez votre proposition : "))  # Demande à l'utilisateur
            
            if proposition < 1 or proposition > 100:  # Vérifie la validité de la proposition
                print("Veuillez entrer un nombre entre 1 et 100.")  # Message d'erreur
                continue
            
            essais += 1  # Incrémente le compteur d'essais
            
            if proposition == juste_prix:  # Vérifie si la proposition est correcte
                message = "Vous avez trouvé le juste prix !!!"  # Message de succès
                print(message)  # Affiche le message de succès
                return message, juste_prix  # Retourne le message et le juste prix
            
            print("Ce n'est pas le bon prix. Essayez encore.")  # Indique que la proposition est incorrecte
        
        if essais == max_essais:  # Si l'utilisateur a épuisé ses essais
            message = f"Vous avez perdu ! Le juste prix était : {juste_prix}"  # Message de perte
            print(message)  # Affiche le message de perte
            return message, juste_prix  # Retourne le message et le juste prix
        
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()  # Demande à l'utilisateur s'il veut rejouer
        if rejouer != 'o':  # Si l'utilisateur ne veut pas rejouer
            continuer = False  # Change la variable pour sortir de la boucle

resultat, prix = juste_prix()
print(f"Résultat du jeu : {resultat} (Juste prix : {prix})" + str(resultat) + " €")
