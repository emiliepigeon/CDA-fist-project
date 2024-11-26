# programmes/horloge_numerique.py

import time

class HorlogeNumerique:
    """Classe pour afficher l'heure actuelle sous forme d'horloge numérique."""

    def afficher(self):
        """Affiche l'heure actuelle en continu jusqu'à ce que l'utilisateur décide d'arrêter."""
        
        while True:
            heure = time.localtime().tm_hour  
            minute = time.localtime().tm_min  
            seconde = time.localtime().tm_sec
            
            print(f"{heure:02}:{minute:02}:{seconde:02}", end="\r")  
            time.sleep(1)  
            
            if input("\nVoulez-vous retourner au menu ? (o/n) : ").lower() != 'n':
                break  
# TODO: Faire que le menu de début s'affiche si o à la question "voulez vousretourner au menu (o/n)?"
