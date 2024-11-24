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

