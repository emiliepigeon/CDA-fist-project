# programmes/gc.py

class GestionnaireContacts:
    """Classe pour gérer un répertoire de contacts."""

    def gestionner(self):
        """Gère les contacts dans un dictionnaire."""
        
        # Je crée un dictionnaire vide pour stocker les contacts.
        contacts = {}
        
        # Je commence une boucle infinie pour permettre à l'utilisateur de gérer les contacts.
        while True: # TODO: changer le true et mettre un condition tant que != du choix 6 rester dans la boucle.
            # J'affiche le menu des options disponibles pour le gestionnaire de contacts.
            print("\n=== Gestionnaire de Contacts ===")
            print("1. Ajouter un contact")  # Option pour ajouter un nouveau contact.
            print("2. Afficher tous les contacts")  # Option pour afficher tous les contacts enregistrés.
            print("3. Quitter")  # Option pour quitter le gestionnaire.# TODO: après ajout des autes options deviendra 6.
            
            
            # Je demande à l'utilisateur de choisir une option parmi celles proposées.
            choix = input("Choisissez une option (1-3) : ")

            # Si l'utilisateur choisit d'ajouter un contact (option 1) = creat.
            if choix == '1':
                # Je demande à l'utilisateur d'entrer le nom du contact.
                nom = input("Entrez le nom du contact : ")
                # Je demande à l'utilisateur d'entrer le numéro de téléphone portable.
                tel = input("Entrez le numéro de téléphone portable : ")
                # Je demande à l'utilisateur d'entrer l'email du contact.
                email = input("Entrez l'email : ")
                
                # J'ajoute le contact au dictionnaire avec le nom comme clé et une liste contenant le téléphone et l'email comme valeur.
                contacts[nom] = [tel, email]
                
                # J'affiche un message confirmant que le contact a été ajouté avec succès.
                print(f"Contact '{nom}' ajouté avec succès.")
            
            # Si l'utilisateur choisit d'afficher tous les contacts (option 2) = liste de contacts.
            elif choix == '2':
                # Je vérifie si le dictionnaire de contacts est vide.
                if not contacts:
                    print("Aucun contact à afficher.")  # Message si aucun contact n'est présent.
                else:
                    # Je parcours chaque contact dans le dictionnaire.
                    for nom, infos in contacts.items():
                        tel, email = infos  # J'extrais le numéro de téléphone et l'email à partir de la liste d'infos.
                        # J'affiche les informations du contact dans un format lisible.
                        print(f"Nom : {nom}, Téléphone : {tel}, Email : {email}")
                        print("--------------------")  # Ligne de séparation entre les contacts.

            # TODO:# elsif choix == '3': Rechercher un contact = search
            # TODO:# elsif choix == '4': Modifier le contact = update
            # TODO:# elsif choix == '6': Suprimer le contact = delete

            # Si l'utilisateur choisit de quitter (option 3) sera à modifier lorsque j'aurai rajouter le sautres options deviendra option 6.
            elif choix == '3':
                break  # Je sors de la boucle et termine la méthode.

            # Si l'utilisateur entre une option invalide.
            else:
                print("Choix invalide.")  # Message d'erreur pour un choix non reconnu.

# TODO: Faire que le menu de début s'affiche à la fin du jeu avec la question "voulez vousretourner au menu (o/n)?"