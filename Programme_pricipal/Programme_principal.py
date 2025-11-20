from Definition.definition import *

if __name__ == "__main__":
    grille_battleship_j1 = [  # La liste du joueur 1 (affiche les bateaux placés)
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],

    ]
    grille_battleship_attaque_j1 = [  # La liste du joueur 1 (affiche les missiles tirés à l'adversère)
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],

    ]
    grille_battleship_j2 = [  # La liste du joueur 2 (affiche les bateaux placés)
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],

    ]
    grille_battleship_attaque_j2 = [  # La liste du joueur 2 (affiche les missiles tirés à l'adversère)
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ]
    # Compteurs
    nombre_bateauj1 = 5
    nombre_bateauj2 = 5
    nb_tour_joueur = 0

    print("Bienvenue a Battleship!")
    print(fonction_tour_joueur(0))

#PHASE PLACER BATEAU POUR CHAQUE JOUEURS (commence par joueur 1)


    #Partie à **Adem** <------------------------------------------------------------------------------------------------


    # demande a l'utilisateur les donnees besoins pour placer les bateaux dans la liste du joueur
    # si il y a une erreur, recommence le placement
    # répéter 5 fois pour chaque joueur
    while True:
        direction = input("Choissisez une direction du premier bateau a 2 cases:")
        ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        #place le bateau
        bateau1_j1 = placer_bateau(grille_battleship_j1, l, c, direction, 2)
        if bateau1_j1 == "Cette emplacement a déja un bateau." or bateau1_j1 == "L'emplacement n'est pas dans la grille." or bateau1_j1 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j1:
                print(ligne)
            break

    while True:
        direction = input("Choissisez une direction du deuxieme bateau a 2 cases:")
        ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        #place le bateau
        bateau2_j1 = placer_bateau(grille_battleship_j1, l, c, direction, 2)
        if bateau2_j1 == "Cette emplacement a déja un bateau." or bateau2_j1 == "L'emplacement n'est pas dans la grille." or bateau2_j1 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j1:
                print(ligne)
            break

    while True:
        direction = input("Choissisez une direction du bateau a 3 cases:")
        ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        #place le bateau
        bateau3_j1 = placer_bateau(grille_battleship_j1, l, c, direction, 3)
        if bateau3_j1 == "Cette emplacement a déja un bateau." or bateau3_j1 == "L'emplacement n'est pas dans la grille." or bateau3_j1 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j1:
                print(ligne)
            break

    while True:
        direction = input("Choissisez une direction du bateau a 4 cases:")
        ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        #place le bateau
        bateau4_j1 = placer_bateau(grille_battleship_j1, l, c, direction, 4)
        if bateau4_j1 == "Cette emplacement a déja un bateau." or bateau4_j1 == "L'emplacement n'est pas dans la grille." or bateau4_j1 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j1:
                print(ligne)
            break

    while True:
        direction = input("Choissisez une direction du bateau a 5 cases:")
        ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        #place le bateau
        bateau5_j1 = placer_bateau(grille_battleship_j1, l, c, direction, 5)
        if bateau5_j1 == "Cette emplacement a déja un bateau." or bateau5_j1 == "L'emplacement n'est pas dans la grille." or bateau5_j1 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j1:
                print(ligne)
            break

    while True:
        direction = input("Choissisez une direction du premier bateau a 2 cases du Joueur 2:")
        ligne_appel = input(" Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input(" Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        # place le bateau
        bateau1_j2 = placer_bateau(grille_battleship_j2, l, c, direction, 2)
        if bateau1_j2 == "Cette emplacement a déja un bateau." or bateau1_j2 == "L'emplacement n'est pas dans la grille." or bateau1_j2 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j2:
                print(ligne)
            break

    while True:
        direction = input(" Choissisez une direction du deuxieme bateau a 2 cases:")
        ligne_appel = input(" Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input(" Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        # place le bateau
        bateau2_j2 = placer_bateau(grille_battleship_j2, l, c, direction, 2)
        if bateau2_j2 == "Cette emplacement a déja un bateau." or bateau2_j2 == "L'emplacement n'est pas dans la grille." or bateau2_j2 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j2:
                print(ligne)
            break

    while True:
        direction = input("Choissisez une direction du premier bateau a 3 cases:")
        ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        # place le bateau
        bateau3_j2 = placer_bateau(grille_battleship_j2, l, c, direction, 3)
        if bateau3_j2 == "Cette emplacement a déja un bateau." or bateau3_j2 == "L'emplacement n'est pas dans la grille." or bateau3_j2 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j2:
                print(ligne)
            break

    while True:
        direction = input("Choissisez une direction du premier bateau a 4 cases:")
        ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        # place le bateau
        bateau4_j2 = placer_bateau(grille_battleship_j2, l, c, direction, 4)
        if bateau4_j2 == "Cette emplacement a déja un bateau." or bateau4_j2 == "L'emplacement n'est pas dans la grille." or bateau4_j2 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j2:
                print(ligne)
            break

    while True:
        direction = input("Choissisez une direction du premier bateau a 5 cases:")
        ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
        colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
        l = int(ligne_appel)
        c = int(colonne_appel)
        # place le bateau
        bateau5_j2 = placer_bateau(grille_battleship_j2, l, c, direction, 5)
        if bateau5_j2 == "Cette emplacement a déja un bateau." or bateau5_j2 == "L'emplacement n'est pas dans la grille." or bateau5_j2 == "Erreur.":
            print("Veuillez réesayer.")
        else:
            for ligne in grille_battleship_j2:
                print(ligne)
            break




    # Partie à **Ludo** <----------------------------------------------------------------------------------------

    # demande a l'utilisateur où tirer son missile (coordonnées)
    n = 1
    fonction_tour_joueur(n)
    # Pour les 2 joueurs

    for i in range(2):
        n += 1
        print(f"Tour du {fonction_tour_joueur(n)}")  # dit quel joueur joue son tour
        try:
            l = int(input("Choissisez une ligne (horizontale) à où tirer le missile : "))
            c = int(input("Choissisez une colone (verticale) à où tirer le missile : "))
            if 0 < c < 9 or 0 < l < 9:
                print("Votre missile à tiré!")
                # Remplace la case dans la grille d'attaque du joueur avec un "hit" ou un "miss"
                tirer_missile(fonction_tour_joueur(n), l, c)
                print("*" * 70)
                # Affiche les résultats du missile tiré
                resultat_missile(fonction_tour_joueur(n), l, c)
                print("*" * 70)
                break
            else:
                print("Vos coordonnées doivent être entre ou égales à 0 et 8")
        except ValueError:
            print("Les coordonnées doivent êtres des nombres!")


    #Partie à **Félix** <--------

    #Remplace la case du bateau coulé par des hashtags
    bateau_atteint(bateau1_j1, bateau2_j1, bateau3_j1, bateau4_j1, bateau5_j1, bateau1_j2, bateau2_j2, bateau3_j2, bateau4_j2, bateau5_j2,
                   nombre_bateauj1, nombre_bateauj2)
    #Affiche le gagnant selon le nombre de bateau restant
    afficher_gagnant(nombre_bateauj1, nombre_bateauj2)










    