# programmes/menu.py

from programmes.calcul_remise import CalculRemise  # Importation des classes nécessaires
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
        print("***************************************")
        print("Menu de l'application :")
        print("0. Quitter")
        print("1. Calcule remise")
        print("2. Lancé de dés")
        print("3. Juste prix")
        print("4. Horloge numérique")
        print("5. Jeu du pendu")
        print("6. Code césar")
        print("7. Gestionnaire de contact")
        print("8. Calculatrice")
        print("***************************************")

        choix = input("Faites votre choix : ")  # Récupère le choix de l'utilisateur

        while choix != "0":  # Continue tant que l'utilisateur ne choisit pas de quitter
            self.gestion_choix(choix)  # Gère le choix de l'utilisateur
            choix = input("Faites votre choix : ")  # Redemande à l'utilisateur son choix

        print("*** FIN DU PROGRAMME ***")  # Message de fin quand l'utilisateur choisit de quitter

    def gestion_choix(self, choix):
        """Gère les différents choix possibles du menu."""
        match choix:  # Utilisation d'un match-case pour gérer les différents choix possibles
            case "1":
                calcul_remise = CalculRemise()  # Crée une instance de CalculRemise
                calcul_remise.calculer()  # Appelle la méthode pour calculer la remise
            case "2":
                lance_des = LanceDes()  # Crée une instance de LanceDes
                lance_des.lancer()  # Appelle la méthode pour lancer un dé       
            case "3":
                juste_prix = JustePrix()  # Crée une instance de JustePrix
                juste_prix.jouer()  # Appelle la méthode pour jouer au juste prix       
            case "4":
                horloge_numerique = HorlogeNumerique()  # Crée une instance d'HorlogeNumerique
                horloge_numerique.afficher()  # Appelle la méthode pour afficher l'horloge numérique       
            case "5":
                trouve_mot = TrouveMot()  # Crée une instance de TrouveMot
                trouve_mot.jouer()  # Appelle la méthode pour jouer au pendu 
            case "6":
                code_cesar = CodeCesar()  # Crée une instance de CodeCesar
                code_cesar.coder()  # Appelle la méthode pour utiliser le code César
            case "7":
                gestionnaire_contacts = GestionnaireContacts()  # Crée une instance de GestionnaireContacts
                gestionnaire_contacts.gestionner()  # Appelle la méthode pour gérer les contacts 
            case "8":
                calculatrice = Calculatrice()  # Crée une instance de Calculatrice
                calculatrice.calculer()  # Appelle la méthode pour effectuer des calculs 
            case _:
                print("Option non valide. Veuillez choisir une option du menu.")  # Message d'erreur si le choix n'est pas valide
