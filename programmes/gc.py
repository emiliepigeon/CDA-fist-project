# programmes/gc.py

class GestionnaireContacts:
    """Classe pour gérer un répertoire de contacts."""

    def gestionner(self):
        """Gère les contacts dans un dictionnaire."""
        
        contacts = {}
        
        while True:
            print("\n=== Gestionnaire de Contacts ===")
            print("1. Ajouter un contact")
            print("2. Afficher tous les contacts")
            print("3. Quitter")

            choix = input("Choisissez une option (1-3) : ")

            if choix == '1':
                nom = input("Entrez le nom du contact : ")
                tel = input("Entrez le numéro de téléphone portable : ")
                email = input("Entrez l'email : ")
                
                contacts[nom] = [tel, email]
                
                print(f"Contact '{nom}' ajouté avec succès.")
            
            elif choix == '2':
                if not contacts:
                    print("Aucun contact à afficher.")
                else:
                    for nom, infos in contacts.items():
                        tel, email = infos
                        print(f"Nom : {nom}, Téléphone : {tel}, Email : {email}")
                        print("--------------------")

            elif choix == '3':
                break
            
            else:
                print("Choix invalide.")
