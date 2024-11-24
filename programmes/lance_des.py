# programmes/lance_des.py

import random  # J'importe le module random qui me permet de générer des nombres aléatoires.

class LanceDes:
    """Classe pour simuler un lancer de dé."""

    def lancer(self):
        """Lance un dé avec un nombre de faces choisi par l'utilisateur."""
        
        # Je demande à l'utilisateur d'entrer le nombre de faces du dé qu'il souhaite lancer.
        faces = int(input("Entrez le nombre de faces du dé (minimum 4) : "))
        
        # Je vérifie si le nombre de faces est inférieur à 4.
        if faces < 4:  
            print("Veuillez entrer un nombre supérieur ou égal à 4.")  # Message d'erreur si l'entrée est invalide.
            return  # Je quitte la méthode car le nombre de faces n'est pas valide.
        
        # Je génère un résultat aléatoire entre 1 et le nombre de faces spécifié par l'utilisateur.
        resultat = random.randint(1, faces)  
        
        # J'affiche le résultat du lancer de dé.
        print(f"Vous avez lancé le dé : {resultat}")  

        # Option pour retourner au menu ou continuer
        self.continuer_ou_menu()  # J'appelle la méthode pour demander à l'utilisateur s'il veut retourner au menu ou relancer.

    def continuer_ou_menu(self):
        """Demande à l'utilisateur s'il souhaite retourner au menu ou continuer."""
        
        choix = input("\nVoulez-vous retourner au menu ? (o/n) : ").lower()  # Je demande à l'utilisateur s'il veut revenir au menu.
        
        if choix == 'o':
            from programmes.menu import Menu  # J'importe la classe Menu pour pouvoir afficher le menu principal.
            menu = Menu()  # Je crée une instance de la classe Menu.
            menu.afficher_menu()  # J'appelle la méthode pour afficher le menu principal à nouveau.
        
        else:
            self.lancer()  # Si l'utilisateur ne choisit pas 'o', je relance la méthode lancer() pour permettre un nouveau lancer de dé.
