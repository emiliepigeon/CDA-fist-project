# programmes/calcul_remise.py

class CalculRemise:
    """Classe pour calculer une remise sur un montant."""

    def calculer(self):
        """Demande à l'utilisateur un montant et un pourcentage de remise, puis affiche le résultat."""
        montant = float(input("Montant : "))  # Demande le montant à l'utilisateur
        remise = float(input("La remise (en %) : "))  # Demande le pourcentage de remise
        
        resultat = montant - (montant * (remise / 100))  # Calcule le prix après remise
        
        print(f"Le prix après remise est : {resultat:.2f} €")  # Affiche le résultat avec deux décimales.
