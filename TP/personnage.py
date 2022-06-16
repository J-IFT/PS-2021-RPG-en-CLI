""" L'énoncé du TP (je fais des commentaires pour une fois, il va neiger) :
Étape 1 : La classe Personnage
Dans un fichier personnage.py ; Créez une classe Personnage
Un personnage à 5 attributs :
• nom : Son nom, Reçu en paramètre
• vie: Ses points de vie (entier), paramètre facultatif 100 par défaut
• mana : Son mana (entier), paramètre facultatif 0 par défaut
• nomArme : Son arme. paramètre facultatif « Épée en bois » par défaut.
• dgArme : Les dégâts de son arme, un entier qui indique le nombre de points de vie enlevé à
chaque coup, paramètre facultatif 10 par défaut.
Les 5 attributs sont privés et ne doivent être manipulables de l’extérieur de la classe.
La classe Personnage à également 7 méthodes qui sont grosso-modo les actions que le personnage
peut effectuer :
• getNom : Accesseur pour lire le nom du personnage
• getPv : Accesseur pour lire les points de vie du personnage
• getMana : Accesseur pour lire niveau de mana du personnage
Ce sont les seuls accesseurs, tout les autres attributs se manipulent via les méthodes dédiés
• recevoirDegats : le personnage prend un certain nombre de dégâts et perd de la vie.
• attaquer : Inflige les dégâts de son arme à un autre personnage.
• changerArme : On change le nom de l'arme et les dégâts qui vont avec.
• estVivant : Indique si le personnage est encore vivant """

""" Pour la partie 2 : Il faut modifier personnage.py pour utiliser la nouvelle classe Arme
Au début du fichier personnage.py ajouter une ligne : from arme import Arme
Remplacez les attributs
• nomArme
• degatsArme
Par un attribut
• arme (de la classe Arme)
Et surtout, faites les modifications nécessaire pour que le programme fonctionne à nouveau. """
## Je m'occupe donc d'ajouter la ligne demandée dans l'énoncé.
from arme import Arme
## Je commence par créer la classe avec les attributs qui correspondent à celle-ci. Vu qu'ils sont privés on doit mettre __ après le self. :
class Personnage:
    def __init__(self,nom,vie=100,mana=0,nomArme="Épée en bois",dgArme=10):
        self.__nom = nom
        self.__vie = vie
        self.__mana = mana
        self.__arme = Arme(nomArme,dgArme)

## La méthode __str__ qui permet un affichage formaté du personnage :
    def __str__(self):
        if self.estVivant():
            etat="Vivant"
        else:
            etat="Mort"
        return("{} ({}) | PV : {} Mana : {} Arme : {} (dg {}) | {}".format(self.__nom,self.__class__.__name__,self.__vie, self.__mana, self.__arme.getNom(), self.__arme.getDg(), etat))

## Les méthodes "accesseurs" :
    def getNom(self):
        return self.__nom
    def getPv(self):
        return self.__vie
    def getMana(self):
        return self.__mana
    def setPv(self, vie):
        self.__vie = vie
    def getArme(self):
        return self.__arme
    def setMana(self,mana):
        self.__mana = mana
    def setArme(self,arme):
        self.__arme = arme

## Les autres méthodes :
## La méthode "recevoirDegats : le personnage prend un certain nombre de dégâts et perd de la vie."
    def recevoirDegats(self,Arme):
        self.__vie-=int(Arme)
        if self.__vie<0:
            self.__vie=0
## La méthode "attaquer : Inflige les dégâts de son arme à un autre personnage."
    def attaquer(self,cible):
        cible.recevoirDegats(self.__arme.getDg())
## La méthode "changerArme : On change le nom de l'arme et les dégâts qui vont avec."
    def changerArme(self,nomArme,dgArme):
            self.__arme = Arme(nomArme,dgArme)
## La méthode "estVivant : Indique si le personnage est encore vivant."
    def estVivant(self):
        if self.__vie>0:
            return True
        else:
            return False

## Le jeu d'essai
if __name__ == '__main__':
    """ Jeu d'essai """
    player1 = Personnage("Bob")
    gobelin = Personnage("Krok le bô", vie=75, nomArme="Epée rouillée", dgArme=15)
    print(player1)
    print(gobelin)
    gobelin.attaquer(player1)
    gobelin.attaquer(player1)
    gobelin.attaquer(player1)
    player1.changerArme("Tronçonneuse", 50)
    player1.attaquer(gobelin)
    player1.attaquer(gobelin)
    print(player1)
    print(gobelin)
    try :
        print(player1.__nom)
    except AttributeError :
        print("Ok, le nom est privé")
