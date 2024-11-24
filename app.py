# app.py

# J'importe la classe Menu depuis le fichier menu.py qui se trouve dans le dossier programmes.
from programmes.menu import Menu  

def main():
    """Point d'entrée de l'application."""

    
    # Crée une instance de la classe Menu.
    # Cela signifie que nous allons pouvoir utiliser toutes les fonctionnalités définies dans la classe Menu.
    application_menu = Menu()  
    
    # Appelle la méthode afficher_menu de l'instance application_menu.
    # Cette méthode est responsable d'afficher le menu à l'utilisateur.
    application_menu.afficher_menu()  

# Ce bloc de code vérifie si ce fichier est exécuté directement (et non importé dans un autre fichier).
if __name__ == "__main__":
    main()  # Si c'est le cas, appelle la fonction principale main pour démarrer l'application.
