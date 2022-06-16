""" Magicien
Partie 1  (faite) :
Pour les magos, c'est plus compliqué … forcément !
Une des différence entre un magicien et un personnage : à la création, les magiciens ont 100 points
de mana.
2eme différence : Les magicien ont un sort de méditation qui leur redonne 40 point de mana
(maximum 100)
Créer un fichier magicien.py qui décrit une classe Magicien qui hérite de Personnage
Méthode mediter
Entrée : -rien-
Sortie : -rien-
Augmente le mana de 40 ; maximum = 100
Partie 2 :
Magicien rouge / Magicien Blanc
Il y a 2 écoles de magie !
La magie blanche (ils lancent des sorts de soin)
La magie rouge (ils lancent des boules de feu)
Votre magicien doit donc se spécialiser !
Et pour ça … on vas faire des héritages d'héritages !
La classe MageBlanc va hériter de Magicien et ajouter la méthode soigner.
Cette méthode double les points de vie (max. 100) de la cible
et coûte 35 points de mana au lanceur.
Si il n'a pas assez de mana, le sort ne fait rien.
La classe MageRouge va hériter de Magicien et ajouter la méthode boulleDeFeu.
Ce sort fait 60 de dégâts à la cible
et coûte 65 points de mana au lanceur.
Si il n'a pas assez de mana, le sort ne fait rien.
A faire : Implémenter les classes MageBlanc et MageRouge dans magicien.py"""

## Je lie les fichiers ensemble grâce à from/import.
from personnage import Personnage
## Je commence par créer la classe avec la méthode demandé dans l'énoncé.
class Magicien(Personnage):
    def __init__(self,nom,vie=100,mana=100,nomArme="Épée en bois",dgArme=10):
        super().__init__(nom,vie,mana,nomArme,dgArme)

    def mediter(self):
        self.setMana(self.getMana()+40)
        if self.getMana()>100:
            self.setMana(100)
## Je m'occupe de la partie 2 de l'énoncé donc de créer les classes des mages.
class MageBlanc(Magicien):
    def soigner(self,cible):
        if self.getMana()>35:
            self.setMana(self.getMana()-35)
            cible.setPv(cible.getPv()*2)
            if cible.getPv()>100:
                cible.setPv(100)
        else:
            print("Pas assez de mana.")

class MageRouge(Magicien):
    def boulleDeFeu(self,cible):
        if self.getMana()>65:
            self.setMana(self.getMana()-65)
            cible.recevoirDegats(60)
        else:
            print("Pas assez de mana.")

## Le jeu d'essai 1 que je remplace par le 2 comme demandé :
if __name__ == '__main__':
    """ Jeu d'essai """
    player1 = Personnage("Bob")
    player4 = MageBlanc("Riri")
    player5 = MageRouge("Fifi")
    player5.boulleDeFeu(player1)
    player4.soigner(player1)
    print(player1)
    player5.boulleDeFeu(player1)
    player4.soigner(player1)
    print(player1)
    print(player4)
    print(player5)
