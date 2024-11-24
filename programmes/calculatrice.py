# programmes/calculatrice.py

class Calculatrice:
    """Classe pour effectuer des calculs de base : addition, soustraction, multiplication et division."""

    def calculer(self):
        """Permet à l'utilisateur d'effectuer des calculs de base en choisissant une opération."""
        
        # Je commence une boucle infinie pour permettre à l'utilisateur de faire plusieurs calculs.
        while True:
            # J'affiche le menu des opérations disponibles.
            print("=== Menu de la Calculatrice ===")
            print("1. Addition")  # Je propose l'option d'addition.
            print("2. Soustraction")  # Je propose l'option de soustraction.
            print("3. Multiplication")  # Je propose l'option de multiplication.
            print("4. Division")  # Je propose l'option de division.
            print("5. Retour au menu principal")  # J'ajoute une option pour retourner au menu principal.
            
            # Je demande à l'utilisateur de choisir une opération parmi celles proposées.
            choix = input("Choisissez une opération (1-5) : ")

            # Je vérifie que le choix fait par l'utilisateur est valide (entre 1 et 5).
            if choix not in ['1', '2', '3', '4', '5']:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")  # Message d'erreur si le choix n'est pas valide.
                continue  # Je redemande à l'utilisateur de faire un choix.

            if choix == '5':  # Si l'utilisateur choisit de retourner au menu principal.
                from programmes.menu import Menu  # J'importe la classe Menu pour pouvoir afficher le menu principal.
                menu = Menu()  # Je crée une instance de la classe Menu.
                menu.afficher_menu()  # J'appelle la méthode pour afficher le menu principal à nouveau.
                return  # Je quitte la méthode calculer() pour ne pas continuer avec d'autres calculs.

            # Je demande à l'utilisateur d'entrer les deux nombres sur lesquels il souhaite effectuer le calcul.
            try:
                nombre1 = float(input("Entrez le premier nombre : "))  # Je convertis l'entrée en nombre flottant pour permettre des calculs décimaux.
                nombre2 = float(input("Entrez le deuxième nombre : "))  # Même conversion pour le deuxième nombre.
            except ValueError:
                print("Veuillez entrer des nombres valides.")  # Si l'utilisateur entre quelque chose qui n'est pas un nombre, j'affiche un message d'erreur.
                continue  # Je redemande les deux nombres.

            # Je commence à effectuer le calcul en fonction du choix de l'utilisateur.
            if choix == '1':  # Si l'utilisateur a choisi l'addition.
                resultat = nombre1 + nombre2  # J'additionne les deux nombres.
                operation = "addition"  # J'enregistre le type d'opération pour l'affichage du résultat.
            elif choix == '2':  # Si l'utilisateur a choisi la soustraction.
                resultat = nombre1 - nombre2  # Je soustrais le deuxième nombre du premier.
                operation = "soustraction"  # J'enregistre le type d'opération pour l'affichage du résultat.
            elif choix == '3':  # Si l'utilisateur a choisi la multiplication.
                resultat = nombre1 * nombre2  # Je multiplie les deux nombres.
                operation = "multiplication"  # J'enregistre le type d'opération pour l'affichage du résultat.
            elif choix == '4':  # Si l'utilisateur a choisi la division.
                if nombre2 == 0:  # Je vérifie si le dénominateur est zéro pour éviter une erreur de division par zéro.
                    print("Erreur : Division par zéro n'est pas autorisée.")  # J'affiche un message d'erreur si c'est le cas.
                    continue  # Je redemande les deux nombres.

                resultat = nombre1 / nombre2  # Je divise le premier nombre par le deuxième si tout est valide.
                operation = "division"  # J'enregistre le type d'opération pour l'affichage du résultat.

            # J'affiche le résultat final du calcul avec une phrase explicative et un formatage à deux décimales.
            print(f"Le résultat de la {operation} entre {nombre1} et {nombre2} est : {resultat:.2f}")  

