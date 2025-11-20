import pytest
from Definition.definition import *


def test_placer_bateau():
    # Arrange
    #Act
    placer_bateau(grille_battleship_j1, 0, 0, "bas", 2)

    # Assert
    assert grille_battleship_j1[0][0] == "^" and grille_battleship_j1[1][0] == "^"

@pytest.mark.parametrize("Joueur, ligne, colonne, message", [
    ("Joueur 1", 1, 1, "Votre missile à tiré"),
    ("Joueur 1", -1, 1, "Vos coordonnées doivent être entre ou égales à 0 et 8"),
    ("Joueur 1", "a", "o", "Les coordonnées doivent êtres des nombres!"),
    ("Joueur 1", 6, 10, "Vos coordonnées doivent être entre ou égales à 0 et 8"),
])
def test_tirer_missile():

    dict_hash = crypt.hasher_mots(mots)

    assert isinstance(dict_hash, dict)
    assert len(dict_hash) == longueur
    if len(dict_hash) != 0:
        assert len(dict_hash[mots[0]]) == 3


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

def test_afficher_gagnant():
    # Arrange
    nombre_bateauj1 = 2
    nombre_bateauj2 = 0
    #Act
    resultat_attendu = "Joueur 1"
    resultat_obtenu = afficher_gagnant(2, 0)
    #Assert
    assert resultat_attendu == resultat_obtenu
