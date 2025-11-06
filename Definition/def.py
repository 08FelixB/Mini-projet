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



def placer_bateau(liste_joueur : list[list[str]],l : int, c: int, direction: str, bateau: int):
    """

    :param liste_joueur: liste du joueur à placer les bateaux
    :param l: ligne du point d'origine du bateau
    :param c: colonne du point d'origine
    :param direction: la direction du bateau
    :param bateau : le nombre de cases du bateau
    :return: la liste mise à jour
    """
    liste_joueur[l][c] = "^"
    try:
        if bateau == 2 and direction == "gauche":
            liste_joueur[l - 1][c] = "^"
        elif bateau == 2 and direction == "bas":
            liste_joueur[l][c - 1] = "^"
        elif bateau == 2 and direction == "droite":
            liste_joueur[l + 1][c] = "^"
        elif bateau == 2 and direction =="haut":
            liste_joueur[l][c + 1] = "^"
        elif bateau == 3 and direction == "gauche":
            liste_joueur[l - 1][c] = "^"
            liste_joueur[l - 2][c] = "^"
        elif bateau == 3 and direction == "bas":
            liste_joueur[l][c - 1] = "^"
            liste_joueur[l][c - 2] = "^"
        elif bateau == 3 and direction == "droite":
            liste_joueur[l + 1][c] = "^"
            liste_joueur[l + 1][c] = "^"
        elif bateau == 3 and direction == "haut":
            liste_joueur[l][c + 1] = "^"
            liste_joueur[l][c + 2] = "^"
        elif bateau == 4 and direction == "gauche":
            liste_joueur[l - 1][c] = "^"
            liste_joueur[l - 2][c] = "^"
            liste_joueur[l - 3][c] = "^"
        elif bateau == 4 and direction == "bas":
            liste_joueur[l][c - 1] = "^"
            liste_joueur[l][c - 2] = "^"
            liste_joueur[l][c - 3] = "^"
        elif bateau == 4 and direction == "droite":
            liste_joueur[l + 1][c] = "^"
            liste_joueur[l + 2][c] = "^"
            liste_joueur[l + 3][c] = "^"
        elif bateau == 4 and direction == "haut":
            liste_joueur[l][c + 1] = "^"
            liste_joueur[l][c + 2] = "^"
            liste_joueur[l][c + 3] = "^"
        elif bateau == 5 and direction == "gauche":
            liste_joueur[l - 1][c] = "^"
            liste_joueur[l - 2][c] = "^"
            liste_joueur[l - 3][c] = "^"
            liste_joueur[l - 4][c] = "^"
        elif bateau == 5 and direction == "bas":
            liste_joueur[l][c - 1] = "^"
            liste_joueur[l][c - 2] = "^"
            liste_joueur[l][c - 3] = "^"
            liste_joueur[l][c - 4] = "^"
        elif bateau == 5 and direction == "droite":
            liste_joueur[l + 1][c] = "^"
            liste_joueur[l + 2][c] = "^"
            liste_joueur[l + 3][c] = "^"
            liste_joueur[l + 4][c] = "^"
        elif bateau == 5 and direction == "haut":
            liste_joueur[l][c + 1] = "^"
            liste_joueur[l][c + 2] = "^"
            liste_joueur[l][c + 3] = "^"
            liste_joueur[l][c + 4] = "^"
    except IndexError:
        print("Le bateau dépasse l'arène de jeu.")

    # aller à la colonne de la ligne et insérer ^
    # try:
    #   if bateau = 2 and direction == "gauche":
    #       insert ^ à [ligne de base -1],[colonne de base]
    #   elif bateau = 2 and direction == "bas":
    #       insert ^ à [ligne de base],[colonne de base -1]
    #   elif bateau = 2 and direction == "droite":
    #       insert ^ à [ligne de base + 1],[colonne de base]
    #   elif bateau = 2 and direction == "haut":
    #       insert ^ à [ligne de base],[colonne de base + 1]
    #   if bateau = 3 and direction == "gauche":
    #       insert ^ à [ligne de base -1],[colonne de base]
    #       insert ^ à [ligne de base -2],[colonne de base]
    #   elif bateau = 3 and direction == "bas":
    #       insert ^ à [ligne de base],[colonne de base - 2]
    #       insert ^ à [ligne de base],[colonne de base - 1]
    #   elif bateau = 3 and direction == "droite":
    #       insert ^ à [ligne de base + 1],[colonne de base]
    #       insert ^ à [ligne de base + 2],[colonne de base]
    #   elif bateau = 3 and direction == "haut":
    #       insert ^ à [ligne de base],[colonne de base + 1]
    #       insert ^ à [ligne de base],[colonne de base + 2]
    #   if bateau = 4 and direction == "gauche":
    #       insert ^ à [ligne de base -1],[colonne de base]
    #       insert ^ à [ligne de base -2],[colonne de base]
    #       insert ^ à [ligne de base -3],[colonne de base]
    #   elif bateau = 4 and direction == "bas":
    #       insert ^ à [ligne de base],[colonne de base -1]
    #       insert ^ à [ligne de base],[colonne de base -2]
    #       insert ^ à [ligne de base],[colonne de base -3]
    #   elif bateau = 4 and direction == "droite":
    #       insert ^ à [ligne de base + 1],[colonne de base]
    #       insert ^ à [ligne de base + 2],[colonne de base]
    #       insert ^ à [ligne de base + 3],[colonne de base]
    #   elif bateau = 4 and direction == "haut":
    #       insert ^ à [ligne de base],[colonne de base + 1]
    #       insert ^ à [ligne de base],[colonne de base + 2]
    #       insert ^ à [ligne de base],[colonne de base + 3]
    #   if bateau = 5 and direction == "gauche":
    #       insert ^ à [ligne de base -1],[colonne de base]
    #       insert ^ à [ligne de base -2],[colonne de base]
    #       insert ^ à [ligne de base -3],[colonne de base]
    #       insert ^ à [ligne de base -4],[colonne de base]
    #   elif bateau = 5 and direction == "bas":
    #       insert ^ à [ligne de base],[colonne de base -1]
    #       insert ^ à [ligne de base],[colonne de base -2]
    #       insert ^ à [ligne de base],[colonne de base -3]
    #       insert ^ à [ligne de base],[colonne de base -4]
    #   elif bateau = 5 and direction == "droite":
    #       insert ^ à [ligne de base + 1],[colonne de base]
    #       insert ^ à [ligne de base + 2],[colonne de base]
    #       insert ^ à [ligne de base + 3],[colonne de base]
    #       insert ^ à [ligne de base + 4],[colonne de base]
    #   elif bateau = 5 and direction == "haut":
    #       insert ^ à [ligne de base],[colonne de base + 1]
    #       insert ^ à [ligne de base],[colonne de base + 2]
    #       insert ^ à [ligne de base],[colonne de base + 3]
    #       insert ^ à [ligne de base],[colonne de base + 4]
    # excepté erreur index:
    # print









def bateau_atteint():
    """
    Fonction qui indique que le bateau est atteint complètement
    :return: None
    """
    #Si un bateaux a été atteint complètement, les cases du bateau sont remplacé par des hashtags











def affiche_nombre_bateau_restant(j1, j2):
    """
    Fonction qui affiche le nombre de bateau restant après chaque bateau noyé
    :return: Le nombre de bateau restant du j1 ou du j2
    """
    #Si un des bateaux du j1 a été atteint complètement, affiche le nombre de bateau restant du j1





    #Si un des bateaux du j2 a été atteint complètement, affiche le nombre de bateau restant du j2


    #Si le nombre de bateau restant du j1 ou du j2 est 0, retourne le gagnant







def afficher_gagnant(nombre_bateauj1: int, nombre_bateauj2: int, gagnant1: input, gagnant2: input):
  """
  Fonction qui affiche le gagnant
  :nombre_bateauj1: Le nombre de bateau du joueur 1
  :nombre_bateauj2: Le nombre de bateau du joueur 2
  :return: Le nom du gagnant
  """
  #Si le nombre de bateaux du j1 est plus petit que le nombre de bateaux du j2, le gagnant est j2
  if nombre_bateauj1 == 0:
      return gagnant2
  #Si le nombre de bateaux du j2 est plus petit que le nombre de bateaux du j1, le gagnant est j1
  if nombre_bateauj2 = 0:
     return gagnant1







#-------------------------------------------------------------------------(Les fonctions du bas = Ludovic)--------------
# TOD: crée une fonction pour choisir où tirer le missile
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

    print(f"Tour du {tour_joueur}") # dit quel joueur joue son tour
    if tour_joueur == "Joueur 1":
        # détermine où le jouer 1 tire son missile (en utilisant sa propre grille d'attaque)
        grille_battleship_attaque_j1[l][c] = missile
        # affiche où le missile à été lancé
        print("Voici où vous avez tirer votre missile : ")
        for ligne in grille_battleship_attaque_j1:
            print(ligne)
        # détermine où le jouer 2 tire son missile (en utilisant sa propre grille d'attaque)
    if tour_joueur == "Joueur 2":
        grille_battleship_attaque_j2[l][c] = missile
        # affiche où le missile à été lancé
        print("Voici où vous avez tirer votre missile : ")
        for ligne in grille_battleship_attaque_j2:
            print(ligne)




# TOD: crée une fonction pour dire si un missile à atteint un bateau (ou s'il à tirer le vide) en changeant
#  le str de la case en fonction de s'il a frapper un bateau ou non.
def resultat_missile(tour_joueur: str, l: int, c: int) -> str:
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
            grille_battleship_attaque_j1[l][c] =
            # affiche où le missile à été lancé
            print("Voici où vous avez tirer votre missile : ")
            for ligne in grille_battleship_attaque_j1:
                print(ligne)
            # détermine si le missile tiré par le jouer 2 frappe un bateau ou non(en utilisant sa propre grille d'attaque)
        if tour_joueur == "Joueur 2" and grille_battleship_j1[l][c] == "^":
            grille_battleship_attaque_j2[l][c] = hit
            # affiche où le missile à été lancé
            print("Voici où vous avez tirer votre missile : ")
            for ligne in grille_battleship_attaque_j2:
                print(ligne)




