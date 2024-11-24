# programmes/lance_des.py

import random

class LanceDes:
    """Classe pour simuler un lancer de dé."""

    def lancer(self):
        """Lance un dé avec un nombre de faces choisi par l'utilisateur."""
        
        faces = int(input("Entrez le nombre de faces du dé (minimum 4) : "))
        
        if faces < 4:
            print("Veuillez entrer un nombre supérieur ou égal à 4.")
            return
        
        resultat = random.randint(1, faces)  
        
        print(f"Vous avez lancé le dé : {resultat}")  
