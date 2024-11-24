# app.py

from programmes.menu import Menu  # J'importe la classe Menu depuis le fichier menu.py

def main():
    """Point d'entrée de l'application."""
    application_menu = Menu()  # Crée une instance de la classe Menu
    application_menu.afficher_menu()  # Affiche le menu

if __name__ == "__main__":
    main()  # Appelle la fonction principale si ce fichier est exécuté directement
