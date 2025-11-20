import pytest
from Definition.definition import *


def test_placer_bateau():
    #Arrange
    #Act
    placer_bateau(grille_battleship_j1, 0, 0, "bas", 2)

    # Assert
    assert grille_battleship_j1[0][0] == "^" and grille_battleship_j1[1][0] == "^"

@pytest.mark.parametrize("joueur, ligne, colonne, message_attendu", [
    ("Joueur 1", 1, 1, "Votre missile à tiré"),
    ("Joueur 1", -1, 1, "Vos coordonnées doivent être entre ou égales à 0 et 8"),
    ("Joueur 2", "a", "o", "Les coordonnées doivent êtres des nombres!"),
    ("Joueur 2", 6, 10, "Vos coordonnées doivent être entre ou égales à 0 et 8"),
])
def test_tirer_missile(joueur, ligne, colonne, message_attendu):



    assert isinstance(joueur, str)
    assert 0 < ligne < 9 or 0 < colonne < 9
    assert ligne.isdecimal() == True
    assert colonne.isdecimal() == True


@pytest.mark.parametrize("initial, nb_cesar, chaine_attendue",[
    ("abcde", 2, "cdefg"),
    ("abcde", 0, "abcde"),
    ("abcde", 10, "klmno"),
    ("abcde", 26, "abcde"),
    ("cdefg", -2, "abcde"),
    ("zoo", 13, "mbb")
])
def test_chiffrement_cesar(initial, nb_cesar, chaine_attendue):

    chaine_cesar = crypt.chiffrement_cesar(initial, nb_cesar)

    assert isinstance(chaine_cesar, str)
    assert len(chaine_cesar) == len(initial)
    assert chaine_cesar == chaine_attendue

def test_bateau_atteint(bateau1_j1, bateau2_j1, bateau3_j1, bateau4_j1, bateau5_j1,
    bateau1_j2, bateau2_j2, bateau3_j2, bateau4_j2, bateau5_j2, nombre_bateauj1, nombre_bateauj2):

    #Arrange
    bateau1_j1 = "*"
    nombre_bateauj1 = 4
    nombre_bateauj2 = 5
    #Act
    resultat = bateau1_j1 = "#"
    resultat_attendu = bateau_atteint(bateau1_j1, bateau2_j1, bateau3_j1, bateau4_j1, bateau5_j1,
    bateau1_j2, bateau2_j2, bateau3_j2, bateau4_j2, bateau5_j2, nombre_bateauj1, nombre_bateauj2)
    #Assert
    assert resulat == resultat_attendu



def test_afficher_gagnant():
    # Arrange
    nombre_bateauj1 = 2
    nombre_bateauj2 = 0
    #Act
    resultat_attendu = "Joueur 1"
    resultat_obtenu = afficher_gagnant(2, 0)
    #Assert
    assert resultat_attendu == resultat_obtenu

