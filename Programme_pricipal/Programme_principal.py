from Definition.definition import placer_bateau, resultat_missile, bateau_atteint

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




print("Bienvenue a Battleship!")
direction = input("Choissisez une direction du premier bateau a 2 cases:")
ligne_appel = input("Choissisez une ligne pour placer la queue du bateau.")
colonne_appel = input("Choissisez une colonne pour placer la queue du bateau.")
l = int(ligne_appel)
c = int(colonne_appel)
bateau1_j1 = placer_bateau(grille_battleship_j1, l, c, direction, 2)
for ligne in grille_battleship_j1:
    print(ligne)









    