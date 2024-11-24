# programmes/menu.py

# J'importe les classes nécessaires depuis d'autres fichiers du projet.
from programmes.calcul_remise import CalculRemise  
from programmes.lance_des import LanceDes
from programmes.juste_prix import JustePrix
from programmes.horloge_numerique import HorlogeNumerique
from programmes.trouve_mot import TrouveMot
from programmes.code_cesar import CodeCesar
from programmes.gc import GestionnaireContacts
from programmes.calculatrice import Calculatrice

class Menu:
    """Classe pour gérer le menu de l'application."""

    def afficher_menu(self):
        """Affiche le menu principal et demande à l'utilisateur de faire un choix."""
        
        # J'affiche une ligne de séparation pour rendre le menu plus lisible.
        print("***************************************")
        print("Menu de l'application :")
        
        # J'affiche les options disponibles dans le menu.
        print("0. Quitter")  # Option pour quitter l'application.
        print("1. Calcule remise")  # Option pour calculer une remise.
        print("2. Lancé de dés")  # Option pour lancer un dé.
        print("3. Juste prix")  # Option pour jouer au jeu du juste prix.
        print("4. Horloge numérique")  # Option pour afficher l'horloge numérique.
        print("5. Jeu du pendu")  # Option pour jouer au pendu.
        print("6. Code césar")  # Option pour utiliser le code César.
        print("7. Gestionnaire de contact")  # Option pour gérer les contacts.
        print("8. Calculatrice")  # Option pour utiliser la calculatrice.
        print("***************************************")

        # Je récupère le choix de l'utilisateur via une entrée clavier.
        choix = input("Faites votre choix : ")  

        # Je commence une boucle qui continue tant que l'utilisateur ne choisit pas de quitter (option "0").
        while choix != "0":  
            self.gestion_choix(choix)  # J'appelle la méthode pour gérer le choix de l'utilisateur.
            choix = input("Faites votre choix : ")  # Je redemande à l'utilisateur son choix.

        # Je montre un message lorsque l'utilisateur choisit de quitter le programme.
        print("*** FIN DU PROGRAMME ***")  

    def gestion_choix(self, choix):
        """Gère les différents choix possibles du menu."""
        
        match choix:  # J'utilise un match-case pour gérer les différents choix possibles.
            case "1":
                calcul_remise = CalculRemise()  # Je crée une instance de la classe CalculRemise.
                calcul_remise.calculer()  # J'appelle la méthode pour calculer la remise.
            case "2":
                lance_des = LanceDes()  # Je crée une instance de la classe LanceDes.
                lance_des.lancer()  # J'appelle la méthode pour lancer un dé.       
            case "3":
                juste_prix = JustePrix()  # Je crée une instance de la classe JustePrix.
                juste_prix.jouer()  # J'appelle la méthode pour jouer au juste prix.       
            case "4":
                horloge_numerique = HorlogeNumerique()  # Je crée une instance de la classe HorlogeNumerique.
                horloge_numerique.afficher()  # J'appelle la méthode pour afficher l'horloge numérique.       
            case "5":
                trouve_mot = TrouveMot()  # Je crée une instance de la classe TrouveMot.
                trouve_mot.jouer()  # J'appelle la méthode pour jouer au pendu. 
            case "6":
                code_cesar = CodeCesar()  # Je crée une instance de la classe CodeCesar.
                code_cesar.coder()  # J'appelle la méthode pour utiliser le code César.
            case "7":
                gestionnaire_contacts = GestionnaireContacts()  # Je crée une instance de la classe GestionnaireContacts.
                gestionnaire_contacts.gestionner()  # J'appelle la méthode pour gérer les contacts. 
            case "8":
                calculatrice = Calculatrice()  # Je crée une instance de la classe Calculatrice.
                calculatrice.calculer()  # J'appelle la méthode pour effectuer des calculs. 
            case _:
                # Je montre un message d'erreur si le choix n'est pas valide ou reconnu.
                print("Option non valide. Veuillez choisir une option du menu.")
