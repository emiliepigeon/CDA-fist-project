# programmes/trouve_mot.py

import random  # J'importe le module random pour choisir un mot aléatoire.

class TrouveMot:
    """Classe pour jouer au jeu du pendu."""

    def jouer(self):
        """Joue au jeu du pendu où l'utilisateur doit deviner un mot."""
        
        # Je définis une liste de mots parmi lesquels le jeu choisira.
        mots = ["CHAT", "BANANE", "SUPERFETATOIRE", "LICORNE", "CON"]
        
        # Je choisis un mot aléatoire dans la liste des mots.
        mot_a_trouver = random.choice(mots)
        
        # Je crée une liste de lettres trouvées, initialisée avec des underscores (_).
        lettres_trouvees = ["_"] * len(mot_a_trouver)
        
        # Je fixe le nombre d'essais restants à 5.
        essais_restants = 5
        
        # Je commence une boucle qui continue tant qu'il reste des essais.
        while essais_restants > 0:
            # J'affiche le mot à deviner, en remplaçant les lettres non trouvées par des underscores.
            print("Mot à deviner :", " ".join(lettres_trouvees))
            
            # Je demande à l'utilisateur de deviner une lettre.
            lettre = input("Devinez une lettre : ").upper()  # Je convertis la lettre en majuscule.
            
            # Je vérifie si la lettre devinée est dans le mot à trouver.
            if lettre in mot_a_trouver:
                # Si la lettre est correcte, je mets à jour la liste des lettres trouvées.
                for index, char in enumerate(mot_a_trouver):
                    if char == lettre:
                        lettres_trouvees[index] = lettre
                
                # Je vérifie si toutes les lettres ont été trouvées.
                if "_" not in lettres_trouvees:
                    print(f"Félicitations ! Vous avez trouvé le mot : {mot_a_trouver}")  # Message de victoire.
                    return  # Je quitte la méthode car le jeu est terminé.
            
            else:
                # Si la lettre n'est pas dans le mot, je décrémente le nombre d'essais restants.
                essais_restants -= 1
            
            # Si l'utilisateur n'a plus d'essais restants, j'affiche un message de perte.
            if essais_restants == 0:
                print(f"Vous avez perdu ! Le mot était : {mot_a_trouver}")  
