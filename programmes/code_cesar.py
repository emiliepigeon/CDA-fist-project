# programmes/code_cesar.py

class CodeCesar:
    """Classe pour chiffrer un message avec le code César."""

    def coder(self):
        """Chiffre un mot en utilisant le chiffrement César."""
        
        mot = input("Entrez le mot à coder (MAJUSCULES uniquement) : ")
        
        decalage = int(input("Entrez le décalage (nombre entier) : "))
        
        mot_code = ""
        
        for char in mot:
            if char.isalpha():
                base = ord('A')
                char_code = chr((ord(char) - base + decalage) % 26 + base)
                mot_code += char_code
        
        print(f"Le mot codé est : {mot_code}")
