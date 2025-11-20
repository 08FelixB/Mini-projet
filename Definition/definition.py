grille_battleship_j1 = [ # La liste du joueur 1 (affiche les bateaux placés)
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
grille_battleship_attaque_j1 = [ # La liste du joueur 1 (affiche les missiles tirés à l'adversère)
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
grille_battleship_j2 = [ # La liste du joueur 2 (affiche les bateaux placés)
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
grille_battleship_attaque_j2 = [ # La liste du joueur 2 (affiche les missiles tirés à l'adversère)
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
# -----------------------------------------------------------------(grilles en haut = ludo)-----------------------------




def afficher_cases(tour_joueur): # Adem
    """

    :param tour_joueur: le tour de quel joueur.
    :return:
    """
    if tour_joueur == "Joueur 1":
        print(grille_battleship_j1)
    elif tour_joueur == "Joueur 2":
        print(grille_battleship_j2)
    else:
        print("Ce joueur n'existe pas.")



def placer_bateau(liste_joueur : list[list[str]],l, c, direction: str, bateau: int):
#def placer_bateau(bateau:int, l, c):
    """
    :param liste_joueur: liste du joueur à placer les bateaux
    :param l: ligne du point d'origine du bateau
    :param c: colonne du point d'origine
    :param direction: la direction du bateau
    :param bateau : le nombre de cases du bateau
    :return: la liste mise à jour
    """


    if liste_joueur[l][c] == "^":
        print("Cette emplacement a déja un bateau.")
        return "Erreur."

    try:
        liste_joueur[l][c] = "^"
    except IndexError:
        print("L'emplacement n'est pas dans la grille.")
        return "Erreur."

    try:
        if bateau == 2 and direction == "gauche":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l][c - 1] == "^":
                        return "Erreur."
                    liste_joueur[l][c - 1] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l][c - 1]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue


        if bateau == 2 and direction == "droite":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l][c + 1] == "^":
                        return "Erreur."
                    liste_joueur[l][c + 1] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l][c + 1]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue


        if bateau == 2 and direction == "bas":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l + 1][c] == "^":
                        return "Erreur."
                    liste_joueur[l + 1][c] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l + 1][c]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue


        if bateau == 2 and direction == "haut":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l - 1][c] == "^":
                        return "Erreur."
                    liste_joueur[l - 1][c] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l - 1][c]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue


        if bateau == 3 and direction == "gauche":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l][c - 1] == "^" or liste_joueur[l][c - 2] == "^":
                        return "Erreur."
                    liste_joueur[l][c - 1] = "^"
                    liste_joueur[l][c - 2] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l][c - 1], liste_joueur[l][c - 2]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 3 and direction == "droite":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l][c + 1] == "^" or liste_joueur[l][c + 2] == "^":
                        return "Erreur."
                    liste_joueur[l][c + 1] = "^"
                    liste_joueur[l][c + 2] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l][c + 1], liste_joueur[l][c + 2]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 3 and direction == "bas":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l + 1][c] == "^" or liste_joueur[l + 2][c] == "^":
                        return "Erreur."
                    liste_joueur[l + 1][c] = "^"
                    liste_joueur[l + 2][c] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l + 1][c], liste_joueur[l + 2][c]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 3 and direction == "haut":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l - 1][c] == "^" or liste_joueur[l --- 2][c] == "^":
                        return "Erreur."
                    liste_joueur[l - 1][c] = "^"
                    liste_joueur[l - 2][c] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l - 1][c], liste_joueur[l - 2][c]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue


        if bateau == 4 and direction == "gauche":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l][c - 1] == "^" or liste_joueur[l][c - 2] == "^" or liste_joueur[l][c - 3] == "^":
                        return "Erreur."
                    liste_joueur[l][c - 1] = "^"
                    liste_joueur[l][c - 2] = "^"
                    liste_joueur[l][c - 3] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l][c - 1], liste_joueur[l][c - 2], liste_joueur[l][c - 3]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 4 and direction == "droite":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l][c + 1] == "^" or liste_joueur[l][c + 2] == "^" or liste_joueur[l][c + 3] == "^":
                        return "Erreur."
                    liste_joueur[l][c + 1] = "^"
                    liste_joueur[l][c + 2] = "^"
                    liste_joueur[l][c + 3] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l][c + 1], liste_joueur[l][c + 2], liste_joueur[l][c + 3]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 4 and direction == "bas":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l + 1][c] == "^" or liste_joueur[l + 2][c] == "^" or liste_joueur[l + 3][c] == "^":
                        return "Erreur."
                    liste_joueur[l + 1][c] = "^"
                    liste_joueur[l + 2][c] = "^"
                    liste_joueur[l + 3][c] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l + 1][c], liste_joueur[l + 2][c], liste_joueur[l + 3][c]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 4 and direction == "haut":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l - 1][c] == "^" or liste_joueur[l - 2][c] == "^" or liste_joueur[l - 3][c] == "^":
                        return "Erreur."
                    liste_joueur[l - 1][c] = "^"
                    liste_joueur[l - 2][c] = "^"
                    liste_joueur[l - 3][c] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l - 1][c], liste_joueur[l - 2][c], liste_joueur[l - 3][c]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue


        if bateau == 5 and direction == "gauche":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l][c - 1] == "^" or liste_joueur[l][c - 2] == "^" or liste_joueur[l][c - 3] == "^" or liste_joueur[l][c - 4] == "^":
                        return "Erreur."
                    liste_joueur[l][c - 1] = "^"
                    liste_joueur[l][c - 2] = "^"
                    liste_joueur[l][c - 3] = "^"
                    liste_joueur[l][c - 4] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l][c - 1], liste_joueur[l][c - 2], liste_joueur[l][c - 3], liste_joueur[l][c - 4]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 5 and direction == "droite":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l][c + 1] == "^" or liste_joueur[l][c + 2] == "^" or liste_joueur[l][c + 3] == "^" or liste_joueur[l][c + 4] == "^":
                        return "Erreur."
                    liste_joueur[l][c + 1] = "^"
                    liste_joueur[l][c + 2] = "^"
                    liste_joueur[l][c + 3] = "^"
                    liste_joueur[l][c + 4] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l][c + 1], liste_joueur[l][c + 2], liste_joueur[l][c + 3], liste_joueur[l][c + 4]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 5 and direction == "bas":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l + 1][c] == "^" or liste_joueur[l + 2][c] == "^" or liste_joueur[l + 3][c] == "^" or liste_joueur[l + 4][c] == "^":
                        return "Erreur."
                    liste_joueur[l + 1][c] = "^"
                    liste_joueur[l + 2][c] = "^"
                    liste_joueur[l + 3][c] = "^"
                    liste_joueur[l + 4][c] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l + 1][c], liste_joueur[l + 2][c], liste_joueur[l + 3][c], liste_joueur[l + 4][c]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue

        if bateau == 5 and direction == "haut":
            while True:
                if l >= 0 or l <= 8 and c >= 0 or c <= 8:
                    if liste_joueur[l - 1][c] == "^" or liste_joueur[l - 2][c] == "^" or liste_joueur[l - 3][c] == "^" or liste_joueur[l - 4][c] == "^":
                        return "Erreur."
                    liste_joueur[l - 1][c] = "^"
                    liste_joueur[l - 2][c] = "^"
                    liste_joueur[l - 3][c] = "^"
                    liste_joueur[l - 4][c] = "^"
                    bateauliste = [liste_joueur[l][c], liste_joueur[l -- 1][c], liste_joueur[l - 2][c], liste_joueur[l - 3][c], liste_joueur[l - 4][c]]
                    return bateauliste
                else:
                    print("Le bateau n'est pas dans la grille. Veuillez réesayer.")
                    continue
    except IndexError:
        print("Le bateau n'est pas dans la grille.")
        return "Erreur."



def bateau_atteint(bateau1_j1, bateau2_j1, bateau3_j1, bateau4_j1, bateau5_j1,
    bateau1_j2, bateau2_j2, bateau3_j2, bateau4_j2, bateau5_j2, nombre_bateauj1, nombre_bateauj2):
    """
    Fonction qui indique que le bateau est atteint complètement
    :param bateau1_j1: Le bateau 1 du j1
    :param bateau2_j1: Le bateau 2 du j1
    :param bateau3_j1: Le bateau 3 du j1
    :param bateau4_j1: Le bateau 4 du j1
    :param bateau5_j1: Le bateau 5 du j1
    :param bateau1_j2: Le bateau 1 du j2
    :param bateau2_j2: Le bateau 2 du j2
    :param bateau3_j2: Le bateau 3 du j2
    :param bateau4_j2: Le bateau 4 du j2
    :param bateau5_j2: Le bateau 5 du j2
    :param nombre_bateauj1: Le nombre de bateaux du joueur 1
    :param nombre_bateauj2: Le nombre de bateaux du joueur 2
    :return: Le nombre restant de bateaux du joueur 1 et du joueur 2
    """
    #Si le premier bateau a été atteint complètement, les cases du bateau sont remplacé par des hashtags
    if bateau1_j1 == "*":
        bateau1_j1 = bateau1_j1.replace("*", "#")
        nombre_bateauj1 -= 1
        print(f"Bateau restant du joueur 1: {nombre_bateauj1}")
        if bateau2_j1 == "*":
            bateau2_j1 = bateau2_j1.replace("*", "#")
            nombre_bateauj1 -= 1
            print(f"Bateau restant du joueur 1: {nombre_bateauj1}")

        if bateau3_j1 == "*":
            bateau3_j1 = bateau3_j1.replace("*", "#")
            nombre_bateauj1 -= 1
            print(f"Bateau restant du joueur 1: {nombre_bateauj1}")
        if bateau4_j1 == "*":
            bateau4_j1 = bateau4_j1.replace("*", "#")
            nombre_bateauj1 -= 1
            print(f"Bateau restant du joueur 1: {nombre_bateauj1}")
        if bateau5_j1 == "*":
            bateau5_j1 = bateau5_j1.replace("*", "#")
            nombre_bateauj1 -= 1
            print(f"Bateau restant du joueur 1: {nombre_bateauj1}")
        if bateau1_j2 == "*":
            bateau1_j2 = bateau1_j2.replace("*", "#")
            nombre_bateauj2 -= 1
            print(f"Bateau restant du joueur 2: {nombre_bateauj2}")

        if bateau2_j2 == "*":
            bateau2_j2 = bateau2_j2.replace("*", "#")
            nombre_bateauj2 -= 1
            print(f"Bateau restant du joueur 2: {nombre_bateauj2}")

        if bateau3_j2 == "*":
            bateau3_j2 = bateau3_j2.replace("*", "#")
            nombre_bateauj2 -= 1
            print(f"Bateau restant du joueur 2: {nombre_bateauj2}")

        if bateau4_j2 == "*":
            bateau4_j2 = bateau4_j2.replace("*", "#")
            nombre_bateauj2 -= 1
            print(f"Bateau restant du joueur 2: {nombre_bateauj2}")
        if bateau5_j2 == "*":
            bateau5_j2 = bateau5_j2.replace("*", "#")
            nombre_bateauj2 -= 1
            print(f"Bateau restant du joueur 2: {nombre_bateauj2}")

        return bateau1_j1, bateau2_j1, bateau3_j1, bateau4_j1, bateau5_j1,
    bateau1_j2, bateau2_j2, bateau3_j2, bateau4_j2, bateau5_j2, nombre_bateauj1, nombre_bateauj2






























def affiche_nombre_bateau_restant(j1, j2):
    """
    Fonction qui affiche le nombre de bateau restant après chaque bateau noyé
    :return: Le nombre de bateau restant du j1 ou du j2
    """
    #Si un des bateaux du j1 a été atteint complètement, affiche le nombre de bateau restant du j1








    #Si un des bateaux du j2 a été atteint complètement, affiche le nombre de bateau restant du j2


    #Si le nombre de bateau restant du j1 ou du j2 est 0, retourne le gagnant







def afficher_gagnant(nombre_bateauj1: int, nombre_bateauj2: int):
  """
  Fonction qui affiche le gagnant
  :nombre_bateauj1: Le nombre de bateau du joueur 1
  :nombre_bateauj2: Le nombre de bateau du joueur 2
  :return: Le nom du gagnant
  """
  #Si le nombre de bateaux du j1 est plus petit que le nombre de bateaux du j2, le gagnant est j2
  if nombre_bateauj1 == 0:
      gagnant = "Joueur 2"
      print(f"Le gagnant est le {gagnant}")
      return gagnant
  #Si le nombre de bateaux du j2 est plus petit que le nombre de bateaux du j1, le gagnant est j1
  if nombre_bateauj2 == 0:
      gagnant = "Joueur 1"
      print(f"Le gagnant est le {gagnant}")
      return gagnant

  return None







#-------------------------------------------------------------------------(Les fonctions du bas = Ludovic)--------------
# TODO: crée une fonction pour choisir où tirer le missile
def tirer_missile(tour_joueur: str,l: int, c: int) -> None:
    """
    Fonction qui demande au joueur choisir où tirer son missile (tour de l'attaque)
    :param tour_joueur: indique le joueur qui complète son tour (d'attaque)
    :param l: les lignes de la grille
    :param c: les colonnes de la grille
    :return: None
    """
    missile = "@"

    # Dans le code principale : demande au joueur où il veut tirer son missile (l = xyz, c = xyz)


    if tour_joueur == "Joueur 1":
        # détermine où le jouer 1 tire son missile (en utilisant sa propre grille d'attaque)
        grille_battleship_attaque_j1[l][c] = missile
        # affiche où le missile à été lancé
        print("Voici où vous avez tirer votre missile : ")
        for ligne in grille_battleship_attaque_j1:
            print(ligne)
        # détermine où le jouer 2 tire son missile (en utilisant sa propre grille d'attaque)
    elif tour_joueur == "Joueur 2":
        grille_battleship_attaque_j2[l][c] = missile
        # affiche où le missile à été lancé
        print("Voici où vous avez tirer votre missile : ")
        for ligne in grille_battleship_attaque_j2:
            print(ligne)




# TODO: crée une fonction pour dire si un missile à atteint un bateau (ou s'il à tirer le vide) en changeant
#  le str de la case en fonction de s'il a frapper un bateau ou non.
def resultat_missile(tour_joueur: str, l: int, c: int) -> None:
        """
        Fonction qui
        :param tour_joueur: indique le joueur qui complète son tour (d'attaque)
        :param l: les lignes de la grille
        :param c: les colonnes de la grille
        :return: None
        """
        hit = "*"
        miss = "X"

        # Dans le code principale : demande au joueur où il veut tirer son missile (l = xyz, c = xyz)

        print(f"Tour du {tour_joueur}")  # dit quel joueur joue son tour
        if tour_joueur == "Joueur 1":
            # détermine si le missile tiré par le jouer 1 frappe un bateau ou non (en utilisant sa propre grille d'attaque)
            if grille_battleship_j1[l][c] == "^":
                grille_battleship_attaque_j1[l][c] = hit
                # affiche le missile étant "hit" sur la grille d'attaque du joueur
                print("Votre missile a frapper un bateau : ")
                for ligne in grille_battleship_attaque_j1:
                    print(ligne)
            else:
                grille_battleship_attaque_j1[l][c] = miss
                # affiche le missile étant "miss"
                print("Votre missile n'a rien frapper : ")
                for ligne in grille_battleship_attaque_j1:
                    print(ligne)
            # détermine si le missile tiré par le jouer 2 frappe un bateau ou non(en utilisant sa propre grille d'attaque)
        elif tour_joueur == "Joueur 2":
            if grille_battleship_j1[l][c] == "^":
                grille_battleship_attaque_j2[l][c] = hit
                # affiche le missile étant "hit" sur la grille d'attaque du joueur
                print("Votre missile a rien frapper un bateau : ")
                for ligne in grille_battleship_attaque_j2:
                    print(ligne)
            else:
                grille_battleship_attaque_j2[l][c] = miss
                # affiche le missile étant "miss"
                print("Votre missile n'a rien frapper : ")
                for ligne in grille_battleship_attaque_j2:
                    print(ligne)

def fonction_tour_joueur(nb_tour_joueur: int,) -> str:
    """
    Fonction qui determine le tour du joueur (j1 ou j2)
    :param nb_tour_joueur: un nombre pour determiner le tour d'un joueur
    :return: le tour du joueur
    """
    if (nb_tour_joueur % 2) == 0:
        tour_joueur = "Joueur 1"
    else:
        tour_joueur = "Joueur 2"
    return tour_joueur
