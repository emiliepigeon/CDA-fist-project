# programmes/calcul_remise.py

class CalculRemise:
    """Classe pour calculer une remise sur un montant."""

    def calculer(self):
        """Demande à l'utilisateur un montant et un pourcentage de remise, puis affiche le résultat."""
        
        # Je demande à l'utilisateur d'entrer le montant initial sur lequel il souhaite appliquer une remise.
        montant = float(input("Montant : "))  # Je convertis l'entrée en nombre flottant pour permettre des calculs décimaux.
        
        # Je demande à l'utilisateur d'entrer le pourcentage de remise qu'il souhaite appliquer.
        remise = float(input("La remise (en %) : "))  # Je convertis également cette entrée en flottant.
        
        # Je calcule le prix après application de la remise en utilisant la formule appropriée.
        resultat = montant - (montant * (remise / 100))  # Je soustrais la remise du montant initial.
        
        # J'affiche le résultat final avec deux décimales, suivi du symbole euro.
        print(f"Le prix après remise est : {resultat:.2f} €")  

        # J'appelle la méthode pour demander à l'utilisateur s'il veut retourner au menu ou continuer.
        self.continuer_ou_menu()

    def continuer_ou_menu(self):
        """Demande à l'utilisateur s'il souhaite retourner au menu ou continuer."""
        
        # Je demande à l'utilisateur s'il veut retourner au menu principal ou continuer avec un nouveau calcul.
        choix = input("\nVoulez-vous retourner au menu ? (o/n) : ").lower()  # Je convertis la réponse en minuscules pour faciliter la comparaison.
        
        if choix == 'o':
            from programmes.menu import Menu  # J'importe la classe Menu pour pouvoir afficher le menu principal.
            menu = Menu()  # Je crée une instance de la classe Menu.
            menu.afficher_menu()  # J'appelle la méthode pour afficher le menu principal à nouveau.
        
        else:
            self.calculer()  # Si l'utilisateur ne choisit pas 'o', je relance la méthode calculer() pour permettre un nouveau calcul de remise.
