""" Etape 4 : Guerrier
Créer un fichier guerrier.py qui décrit une classe Guerrier qui hérite de Personnage et qui à une
méthode en plus : attaquePuissante
attaquePuissante fonctionne comme attaquer, mais elle inflige 1,5 fois les dégâts de l’arme.
Méthode attaquePuissante
Entrée : Cible (Personnage)
Sortie : -rien-
Appelle la méthode recevoirDegats du personnage reçu en paramètre (avec self.degatsArme * 1,5
en paramètre)
Attention, attaquePuissante doit faire des dégâts entier """

## Je lie les fichiers ensemble grâce à from/import.
from personnage import Personnage
## Je commence par créer la classe avec la méthode demandé dans l'énoncé.
class Guerrier(Personnage):

    def attaquePuissante(self,cible):
        cible.recevoirDegats(int(self.getArme().getDg()*1.5))

## Le jeu d'essai
if __name__ == '__main__':
    """ Jeu d'essai """
    player1 = Personnage("Bob")
    player2 = Guerrier("Bill")
    print(player1)
    print(player2)
    player2.changerArme("epée avec des dg impair pour tester l'arrondi", 15)
    player2.attaquer(player1)
    player2.attaquePuissante(player1)
    try :
        player1.attaquePuissante(player2)
    except AttributeError :
        print("Un simple personnage ne peut faire une attaquePuissante")
        print(player1)
        print(player2)
