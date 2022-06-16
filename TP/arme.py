""" Étape 2 : La classe Arme : arme.py
L’étape 1 comporte une erreur de conception : L’arme (nom & dégâts) est inclus dans la classe
personnage.
Ce qui implique qu’un personnage à au moins (et au plus) une arme.
On vas améliorer ça et « détacher » l’arme du personnage :
Dans un fichier arme.py, créer un classe Arme avec comme attributs :
• nom : Attribut privé reçu en paramètre.
• dg : Attribut privé reçu en paramètre.
et comme méthodes :
• __init__
• getNom
• setNom
• getDg
• setDg
La méthode __init__ sert à créer les 2 attributs privés nom & dg
Les 2 méthodes get* servent à renvoyer les valeurs correspondantes
Les 2 méthodes set* servent à modifier les valeurs correspondantes """

## Je commence par créer la classe avec les attributs qui correspondent à celle-ci. Vu qu'ils sont privés on doit mettre __ après le self. :
class Arme:
    def __init__(self,nom,dg):
        self.__nom = nom
        self.__dg = dg

## Les méthodes "accesseurs" :
    def getNom(self):
        return self.__nom
    def setNom(self, nom):
        self.__nom = nom
    def getDg(self):
        return self.__dg
    def setDg(self, dg):
        self.__dg = dg
