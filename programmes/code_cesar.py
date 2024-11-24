# programmes/code_cesar.py

class CodeCesar:
    """Classe pour chiffrer un message avec le code César."""

    def coder(self):
        """Chiffre un mot en utilisant le chiffrement César."""
        
        # Je demande à l'utilisateur d'entrer le mot à coder. 
        # Je précise que seules les lettres majuscules sont acceptées.
        mot = input("Entrez le mot à coder (MAJUSCULES uniquement) : ")
        
        # Je demande à l'utilisateur d'entrer un décalage, qui doit être un nombre entier.
        decalage = int(input("Entrez le décalage (nombre entier) : "))
        
        # Je crée une chaîne vide pour stocker le mot codé.
        mot_code = ""
        
        # Je commence une boucle pour traiter chaque caractère du mot.
        for char in mot:
            # Je vérifie si le caractère est une lettre (A-Z).
            if char.isalpha():
                # Je définis la base de l'alphabet en utilisant le code ASCII de 'A'.
                base = ord('A')
                
                # Je calcule le code du caractère chiffré.
                # J'utilise la formule pour appliquer le décalage et je m'assure de rester dans les limites de l'alphabet (0-25).
                char_code = chr((ord(char) - base + decalage) % 26 + base)
                
                # J'ajoute le caractère codé à la chaîne mot_code.
                mot_code += char_code
        
        # J'affiche le résultat final, c'est-à-dire le mot codé.
        print(f"Le mot codé est : {mot_code}")
