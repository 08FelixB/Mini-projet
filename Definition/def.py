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

    :param tour_joueur: le tour de quel joueur
    :return:
    """
    if tour_joueur == "Joueur 1":
        print(grille_battleship_j1)
    elif tour_joueur == "Joueur 2":
        print(grille_battleship_j2)
    else:
        print("Ce joueur n'existe pas.")



def placer_bateau(liste_joueur : list[list[str]], coordonées : str, direction):
    """

    :param liste_joueur: liste du joueur
    :param coordonées: points de l'index
    :param direction: la direction à
    :return:
    """
   #






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







def afficher_gagnant():
  """
  Fonction qui affiche le gagnant
  :return: Le nom du gagnant
  """
  #Si le nombre de bateaux du j1 est plus petit que le nombre de bateaux du j2, le gagnant est j2
  if


  #Si le nombre de bateaux du j2 est plus petit que le nombre de bateaux du j1, le gagnant est j1







#-------------------------------------------------------------------------(Les fonctions du bas = Ludovic)--------------
# TODO: crée une fonction pour choisir où tirer le missile
def tirer_missile(ligne: int, colonne: int, missile: str, grille: list[list[str]]) -> None:
    """
    Fonction qui affiche
    :param ligne: les lignes de la grille
    :param colonne: les colonnes de la grille
    :param missile: les coordonnées du missile
    :param grille: la grille
    :return: None
    """






# TODO: crée une fonction pour dire si un missile à atteint un bateau (ou s'il à tirer le vide)
def resultat_missile():



# e




