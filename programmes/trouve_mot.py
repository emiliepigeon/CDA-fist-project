# programmes/trouve_mot.py

import random

class TrouveMot:
    """Classe pour jouer au jeu du pendu."""

    def jouer(self):
        """Joue au jeu du pendu où l'utilisateur doit deviner un mot."""
        
        mots = ["CHAT", "BANANE", "SUPERFETATOIRE", "LICORNE", "CON"]
        
        mot_a_trouver = random.choice(mots)
        lettres_trouvees = ["_"] * len(mot_a_trouver)
        
        essais_restants = 5
        
        while essais_restants > 0:
            print("Mot à deviner :", " ".join(lettres_trouvees))
            
            lettre = input("Devinez une lettre : ").upper()
            
            if lettre in mot_a_trouver:
                for index, char in enumerate(mot_a_trouver):
                    if char == lettre:
                        lettres_trouvees[index] = lettre
                
                if "_" not in lettres_trouvees:
                    print(f"Félicitations ! Vous avez trouvé le mot : {mot_a_trouver}")
                    return
            
            else:
                essais_restants -= 1
            
            if essais_restants == 0:
                print(f"Vous avez perdu ! Le mot était : {mot_a_trouver}")
