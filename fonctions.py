# Fonctionnalité 1 : Calcul de remise => menu.py choix 1
# Définition de la fonction (def) pour calculer une remise
def calcul_remise(_montant, _remise): 
    # Calcul du prix après remise
    resultat = _montant - _montant * (_remise/100)
    # Affichage du résultat
    return print("Le prix de l'article après la remise est de : " + str(resultat) + " €")

###################################################################################################
# Fonctionnalité 2 : Lancé de dés => menu.py choix 2
import random  # Importation du module random pour générer des nombres aléatoires
# Définition de la fonction (def) pour clancer le dé
def lance_des():
    """Cette fonction permet à l'utilisateur de lancer un dé avec un nombre de faces choisi."""
    
    while True:  # Boucle pour permettre à l'utilisateur de rejouer
        # Demande à l'utilisateur combien de faces doit avoir le dé
        faces = int(input("Entrez le nombre de faces du dé (minimum 4) : "))
        
        # Vérifie que le nombre de faces est valide
        if faces < 4:
            print("Veuillez entrer un nombre de faces supérieur ou égal à 4.")
            continue  # Redemande le nombre de faces si moins de 4
        
        # Lance le dé en générant un nombre aléatoire entre 1 et le nombre de faces
        resultat = random.randint(1, faces)
        
        # Affiche le résultat du lancer
        print(f"Vous avez lancé le dé : {resultat}")
        
        # Demande à l'utilisateur s'il veut relancer le dé
        rejouer = input("Voulez-vous lancer à nouveau ? (o/n) : ").lower()
        
        # Si l'utilisateur ne veut pas rejouer, on sort de la boucle
        if rejouer != 'o':
            return print("Le résultat du lancé est de : " + str(resultat) + "pour un dé à " + str(faces) + " faces")
            # Retourne le résultat final du lancer

###################################################################################################
import random  # Importation du module random pour générer des nombres aléatoires

def juste_prix():
    """Cette fonction permet à l'utilisateur de deviner un prix entre 1 et 50 euros."""
    
    continuer = True  # Variable pour contrôler si le jeu continue
    
    while continuer:  # Boucle tant que continuer est vrai
        juste_prix = random.randint(1, 50)  # Générer un juste prix aléatoire
        essais = 0  # Compteur d'essais
        max_essais = 5  # Nombre maximum d'essais autorisés
        
        print("Bienvenue au jeu du juste prix !")  # Message d'accueil
        print("Devinez le prix entre 1 et 50 euros.")  # Instructions
        
        while essais < max_essais:  # Boucle pour les essais
            proposition = int(input("Entrez votre proposition : "))  # Demande à l'utilisateur
            
            if proposition < 1 or proposition > 50:  # Vérifie la validité de la proposition
                print("Veuillez entrer un nombre entre 1 et 50.")  # Message d'erreur
                continue
            
            essais += 1  # Incrémente le compteur d'essais
            
            if proposition == juste_prix:  # Vérifie si la proposition est correcte
                message = "Vous avez trouvé le juste prix !!!"  # Message de succès
                print(message)  # Affiche le message de succès
                return message, juste_prix
            
            # Indication si la proposition est trop basse ou trop haute
            if proposition < juste_prix:
                print("C'est plus !")  # Indique que le juste prix est plus élevé
            else:
                print("C'est moins !")  # Indique que le juste prix est plus bas
        
        if essais == max_essais:  # Si l'utilisateur a épuisé ses essais
            message = f"Vous avez perdu ! Le juste prix était : {juste_prix}"  # Message de perte
            print(message)  # Affiche le message de perte
            return message, juste_prix
        
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()  # Demande à l'utilisateur s'il veut rejouer
        if rejouer != 'o':  # Si l'utilisateur ne veut pas rejouer
            continuer = False  # Change la variable pour sortir de la boucle

###########################################################################################################
# Fonctionnalité 4 : Horloge numérique => menu.py choix 4
import time  # Importation du module time pour accéder à l'heure système

def horloge_numérique():
    """Cette fonction affiche l'heure actuelle sous forme d'horloge numérique."""
    
    while True:  # Boucle pour permettre à l'utilisateur de rester dans l'horloge jusqu'à ce qu'il choisisse de quitter
        # Obtenir l'heure actuelle
        heure = time.localtime().tm_hour  # Récupère l'heure actuelle
        minute = time.localtime().tm_min  # Récupère les minutes actuelles
        seconde = time.localtime().tm_sec  # Récupère les secondes actuelles
        
        # Affiche l'heure au format numérique
        print(f"{heure:02}:{minute:02}:{seconde:02}")  # Affiche l'heure, les minutes et les secondes avec un format à deux chiffres
        
        # Pause d'une seconde avant de mettre à jour l'affichage
        time.sleep(1)  # Attend une seconde

        # Pose la question à l'utilisateur
        choix = input("Voulez-vous retourner au menu ? (o/n) : ").lower()  # Demande à l'utilisateur s'il veut retourner au menu
        
        # Vérifie si l'utilisateur a saisi 'o' ou 'n'
        if choix == 'o':  # Si l'utilisateur veut retourner au menu
            print("Retour au menu...")  # Message indiquant le retour au menu
            break  # Quitte la boucle et termine la fonction
        elif choix == 'n':  # Si l'utilisateur ne veut pas retourner au menu
            print("Vous restez dans l'horloge.")  # Message indiquant que l'utilisateur reste dans l'horloge
            continue  # Continue la boucle pour afficher l'heure encore une fois
        else:
            print("Choix invalide. Veuillez entrer 'o' pour oui ou 'n' pour non.")  # Gestion des entrées invalides

###########################################################################################################
# Fonctionnalité 5 : Jeu du pendu => menu.py choix 5
import random  # Importation du module random pour choisir un mot aléatoire

def trouve_mot():
    """Cette fonction simule un jeu du pendu avec un mot à deviner."""
    
    # Dictionnaire de mots à deviner (sans caractères spéciaux ni accents)
    mots = ["CHAT", "BANANE", "SUPERFETATOIRE", "LICORNE", "CON"]
    
    # Affiche les règles du jeu
    print("Bienvenue au jeu du Pendu !")
    print("Règles du jeu :")
    print("1. Vous devez deviner le mot en proposant des lettres.")
    print("2. Vous avez 5 chances pour vous tromper.")
    print("3. Les mots ne contiennent que des lettres MAJUSCULES.")
    print("4. Les caractères spéciaux et les accents ne sont pas utilisés.")
    
    # Choisir un mot aléatoire dans le dictionnaire
    mot_a_trouver = random.choice(mots)  # Mot à deviner
    lettres_trouvees = ["_"] * len(mot_a_trouver)  # Liste pour afficher les lettres trouvées
    essais_restants = 5  # Nombre d'essais restants
    essais_faibles = []  # Liste pour stocker les lettres déjà essayées

    print("\nLe mot à deviner a", len(mot_a_trouver), "lettres.")  # Indique le nombre de lettres

    while essais_restants > 0:  # Tant que le joueur a des essais restants
        print("Mot à deviner :", " ".join(lettres_trouvees))  # Affiche le mot avec des tirets
        print("Essais restants :", essais_restants)  # Affiche le nombre d'essais restants
        print("Lettres déjà essayées :", " ".join(essais_faibles))  # Affiche les lettres déjà essayées

        # Demande à l'utilisateur de deviner une lettre
        lettre = input("Devinez une lettre : ").upper()  # Convertit la lettre en majuscule

        if len(lettre) != 1 or not lettre.isalpha():  # Vérifie que l'entrée est valide
            print("Veuillez entrer une seule lettre.")  # Message d'erreur
            continue
        
        if lettre in essais_faibles:  # Vérifie si la lettre a déjà été essayée
            print("Vous avez déjà essayé cette lettre.")  # Message d'erreur
            continue
        
        essais_faibles.append(lettre)  # Ajoute la lettre aux essais faibles

        if lettre in mot_a_trouver:  # Si la lettre est dans le mot à trouver
            print("Bien joué ! La lettre", lettre, "est dans le mot.")
            for index, char in enumerate(mot_a_trouver):  # Parcourt chaque caractère du mot
                if char == lettre:  # Si la lettre correspond au caractère du mot
                    lettres_trouvees[index] = lettre  # Remplace le tiret par la lettre trouvée
            
            if "_" not in lettres_trouvees:  # Vérifie si toutes les lettres ont été trouvées
                print("Félicitations ! Vous avez trouvé le mot :", mot_a_trouver)
                break  # Sort de la boucle si le mot est trouvé
        else:
            essais_restants -= 1  # Diminue le nombre d'essais restants
            print("Désolé, la lettre", lettre, "n'est pas dans le mot. Vous perdez une chance.")

    if essais_restants == 0:  # Si le joueur n'a plus d'essais restants
        print("Vous avez perdu ! Le mot était :", mot_a_trouver)  # Message de perte
    
    # Demande à l'utilisateur s'il veut recommencer
    rejouer = input("Voulez-vous recommencer ? (o/n) : ").lower()  
    if rejouer == 'o':  
        trouve_mot()  # Relance une nouvelle partie
    else:
        print("Retour au menu...")  # Message indiquant qu'on retourne au menu

###########################################################################################################
# Fonctionnalité 6 : Code césar => menu.py choix 6
def code_cesar():
    """Cette fonction permet de coder un mot en utilisant le chiffrement de César avec des lettres majuscules uniquement."""
    
    # Demande à l'utilisateur d'entrer le mot à coder
    mot = input("Entrez le mot à coder (uniquement des majuscules) : ")  # Mot à coder
    
    # Vérifie si le mot contient uniquement des majuscules
    if not mot.isupper():  # Si le mot n'est pas en majuscules
        print("Erreur : Veuillez entrer uniquement des lettres MAJUSCULES.")  # Message d'erreur
        return  # Quitte la fonction si l'entrée est invalide

    # Demande à l'utilisateur d'entrer le décalage
    decalage = int(input("Entrez le décalage (nombre entier) : "))  # Décalage pour le chiffrement

    mot_code = ""  # Variable pour stocker le mot codé

    # Parcourt chaque caractère du mot
    for char in mot:
        # Vérifie si le caractère est une lettre majuscule
        if char.isalpha():  # Si c'est une lettre
            # Calcule le décalage pour les lettres majuscules
            base = ord('A')  # Base pour les majuscules
            
            # Applique le décalage et s'assure que cela reste dans l'alphabet
            char_code = chr((ord(char) - base + decalage) % 26 + base)  # Caractère codé
            mot_code += char_code  # Ajoute le caractère codé au mot codé
        else:
            # En théorie, ce cas ne devrait pas se produire car on vérifie les majuscules au début
            mot_code += char  # Ajoute le caractère tel quel (non utilisé ici)

    # Affiche le résultat final
    print(f"Le mot codé est : {mot_code}")  # Affiche le mot codé

###########################################################################################################
# Fonctionnalité 7 : Gestionnaire de contacts => menu.py choix 7

###########################################################################################################
# Fonctionnalité 5 : Jeu du pendu => menu.py choix 5

###########################################################################################################
# Fonctionnalité 6 : Code césar => menu.py choix 6

###########################################################################################################
# Fonctionnalité 8 : Baccalauréat => menu.py choix 8