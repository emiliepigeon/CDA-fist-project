# programmes/juste_prix.py

import random

class JustePrix:
    """Classe pour jouer au jeu du juste prix."""

    def jouer(self):
        """Joue au jeu du juste prix où l'utilisateur doit deviner un prix."""
        
        prix = random.randint(1, 100)
        essais_restants = 5
        
        while essais_restants > 0:
            proposition = int(input("Devinez le prix entre 1 et 100 : "))
            
            if proposition < prix:
                print("C'est plus !")
            elif proposition > prix:
                print("C'est moins !")
            else:
                print(f"Bravo ! Vous avez trouvé le juste prix : {prix}")
                return
            
            essais_restants -= 1
        
        print(f"Vous avez perdu ! Le juste prix était : {prix}")
