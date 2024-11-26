# programmes/juste_prix.py

import random  # J'importe le module random pour générer un prix aléatoire.

class JustePrix:
    """Classe pour jouer au jeu du juste prix."""

    def jouer(self):
        """Joue au jeu du juste prix où l'utilisateur doit deviner un prix."""
        
        # Je génère un prix aléatoire entre 1 et 50.
        prix = random.randint(1, 50)
        
        # Je fixe le nombre d'essais restants à 5.
        essais_restants = 5
        
        # Je commence une boucle qui continue tant qu'il reste des essais.
        while essais_restants > 0:
            # Je demande à l'utilisateur de deviner le prix.
            proposition = int(input("Devinez le prix entre 1 et 50 : "))  # Je convertis l'entrée en entier.
            
            # Je vérifie si la proposition de l'utilisateur est inférieure au prix.
            if proposition < prix:
                print("C'est plus !")  # Indication que le prix est plus élevé.
            # Je vérifie si la proposition de l'utilisateur est supérieure au prix.
            elif proposition > prix:
                print("C'est moins !")  # Indication que le prix est plus bas.
            # Si la proposition est égale au prix, l'utilisateur a gagné.
            else:
                print(f"Bravo ! Vous avez trouvé le juste prix : {prix}")  # Message de félicitations.
                return  # Je quitte la méthode car le jeu est terminé.
            
            # Je décrémente le nombre d'essais restants après chaque tentative.
            essais_restants -= 1
        
        # Si l'utilisateur n'a pas trouvé le prix après ses essais, je lui indique qu'il a perdu.
        print(f"Vous avez perdu ! Le juste prix était : {prix}")  

# TODO: Faire que le menu de début s'affiche à la fin du jeu avec la question "voulez vousretourner au menu (o/n)?"