from Definition.definition import placer_bateau
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
    bateau2n1_j1 = placer_bateau(grille_battleship_j1, 0, 8, "gauche", 2)
    for ligne in grille_battleship_j1:
        print(ligne)

    