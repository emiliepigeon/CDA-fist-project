# menu.py

from fonctions import calcul_remise, lance_des, juste_prix, horloge_numérique, trouve_mot, code_cesar  
# J'importe le fichier fonctions.py pour utiliser ses fonctions

def afficher_menu():
# J'utilise des print pour afficher chaque ligne de mon menu
    """Affiche le menu principal et demande à l'utilisateur de faire un choix."""
    print("***************************************")
    print("Menu de l'application :")
    print("0. Quitter")
    print("1. Calcule remise") # Autre Addition
    print("2. Lancé de dés") # Autre Soustraction
    print("3. Juste prix") # Autre Multiplication
    print("4. Horloge numérique")# Autre division
    print("5. Jeu du pendu") # Autre 
    print("6. Code césar") # Autre 
    print("7. Gestionnaire de contact") # Autre 
    # print("8. Baccalauréat")
    print("***************************************")

    return input("Faites votre choix : ")

# J'affiche mon menu pour la première fois et je récupère le choix de l'utilisateur
choix = afficher_menu()

# Je commence une boucle qui continuera tant que l'utilisateur ne choisit pas de quitter (choix "0")
while choix != "0":
    
    match (choix):  # J'utilise un match-case pour gérer les différents choix possibles
        case "1":
            montant = int(input("Montant : "))  # Je demande le montant à l'utilisateur
            remise = int(input("La remise : "))  # Je demande le pourcentage de remise
            calcul_remise(montant, remise)  # J'appelle la fonction pour calculer la remise
        case "2":
            lance_des()
            # J'appelle la fonction pour lancer un dé       
        case "3":
            juste_prix()
            # J'appelle la fonction pour jouer au juste prix       
        case "4":
            horloge_numérique()
            # J'appelle la fonction pour afficher l'horloge numérique       
        case "5":
            trouve_mot()
            # J'appelle la fonction pour jouer au pendu 
        case "6":
            code_cesar()
            # J'appelle la fonction pour utiliser le code César
        # case "7":
            # Appel au gestionnaire de contacts
        case _:
            print("Option non valide. Veuillez choisir une option du menu.")  # Message d'erreur si le choix n'est pas valide
    
    choix = afficher_menu()  # Redemande à l'utilisateur son choix

# Quand l'utilisateur choisit de quitter (choix "0"), j'affiche un message de fin
print("*** FIN DU PROGRAMME ***")