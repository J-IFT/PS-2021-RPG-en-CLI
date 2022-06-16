# PS-2021-RPG-en-CLI

*PS = Projet Scolaire*

## 📚 Projet Scolaire | Réalisation d'un RPG en CLI 

Mars 2021

Individuel

### 📎 Vidéo de démonstration :

Un aperçu en vidéo, c'est toujours mieux !

https://youtu.be/zE-BXBalkRg

### 📌 Consignes du projet :

Étape 1 - La classe Personnage :

Dans un fichier personnage.py : créez une classe Personnage.

Un personnage à 5 attributs :

• nom : Son nom, Reçu en paramètre

• vie: Ses points de vie (entier), paramètre facultatif 100 par défaut

• mana : Son mana (entier), paramètre facultatif 0 par défaut

• nomArme : Son arme. paramètre facultatif « Épée en bois » par défaut.

• dgArme : Les dégâts de son arme, un entier qui indique le nombre de points de vie enlevé à chaque coup, paramètre facultatif 10 par défaut.

Les 5 attributs sont privés et ne doivent pas être manipulables de l’extérieur de la classe.

La classe Personnage à également 7 méthodes qui sont grosso-modo les actions que le personnage peut effectuer :

• getNom : Accesseur pour lire le nom du personnage.

• getVie : Accesseur pour lire les points de vie du personnage.

• getMana : Accesseur pour lire niveau de mana du personnage.

Ce sont les seuls accesseurs1, tout les autres attributs se manipulent via les méthodes dédiés.

• recevoirDegats : le personnage prend un certain nombre de dégâts et perd de la vie.

• attaquer : Inflige les dégâts de son arme à un autre personnage.

• changerArme : On change le nom de l'arme et les dégâts qui vont avec.

• estVivant : Indique si le personnage est encore vivant.

Méthode RecevoirDegats :

Entrée : degats (int)
Sortie : -rien-
Enlève les points de dégâts reçu en paramètre à l’attribut vie.
S’assure que vie ne soit jamais négatif.
Méthode attaquer
Entrée : cible (Personnage)
Sortie : -rien-
Appelle la méthode recevoirDegats du personnage reçu en paramètre (avec son propre attribut degatsArme en paramètre)
Méthode changerArme
Entrée : nomArme (string), dgArme (int)
Sortie : -rien-
Met les 2 paramètres reçu dans nomArme et degatsArme
Méthode estVivant
Entrée : -rien-
Sortie : Booléen
Renvoi True si vie est > zéro.
False sinon

Méthode __str__ :

La classe à aussi une méthode __str__ qui permet un affichage formaté du personnage.
"{} ({}) | PV : {} Mana : {} Arme : {} (dg {}) | {}"
Ou les paramètres valent les infos suivantes :
• Nom du personnage
• Nom de la classe (a vous de chercher comment la récupérer �)
• Vie
• Mana
• Nom de l’arme
• Dg de l’arme
• « Vivant » ou « Mort »

Étape 2 - La classe Arme :

arme.py
L’étape 1 comporte une erreur de conception : L’arme (nom & dégâts) est inclus dans la classe personnage. Ce qui implique qu’un personnage à au moins (et au plus) une arme. 
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
Les 2 méthodes set* servent à modifier les valeurs correspondantes

personnage.py

Il faut modifier personnage.py pour utiliser la nouvelle classe Arme
Au début du fichier personnage.py ajouter une ligne :
from arme import Arme
Remplacez les attributs
• nomArme
• degatsArme
Par un attribut
• arme (de la classe Arme)
Et surtout, faites les modifications nécessaire pour que le programme fonctionne à nouveau.
Ex : Dans le constructeur de Personnage, remplacez 
self.__nomArme = nomArme
self.__dgArme = dgArme
par
self.__arme = Arme(nomArme, dgArme)
Etc ..

Étape 3 :

RPG.py
Écrire un fichier RPG.py qui permet d’utiliser la classe de personnage dans un micro-jeu-de-roleen-ligne-de-commande-pour-les-nuls.
Demander au joueur le nom de son personnage.
Instancier un objet de la classe Personnage avec 120 points de vie.

Demander dans un menu qui l’on veut combattre

1 - un gobelin (75 pv, armé d’un gourdin (15 dg))
2 - un orc (100 pv, armé d’une épée rouillée (20 dg))
3 - un troll (200 pv, armé d’une hache (30 dg))
0 – Quitter le jeu

Attention, votre code doit être « résistant aux erreurs de saisie » et n’accepter que les choix 0 ~ 3.
Puis boucler sur un second menu qui

– Affiche le statut de chacun des 2 personnages
– Demande au joueur de choisir entre
1 - Attaquer
2 - Changer d'arme (Épée, 45 dg)
0 - Abandonner

Arrêtez quand (au moins) l'un des 2 est mort.
Affichez le vainqueur.
Retourner à l’étape 2.
Règle : Si Le joueur change d’arme l’adversaire l’attaque une fois « gratuitement ».
Règle : Abandon = défaite ; match nul = défaite2.
Attention : Votre jeu doit être « résistant à une erreur de saisie ».

Étape 4 :

Notre classe personnage est sympa … mais un peu légère.
Je veut, par exemple, des magiciens (qui lancent des sort en utilisant du mana), des guerriers qui ont des attaques spéciales …
On vas créer 2 classes qui héritent, chacune, de Personnage.

- Guerrier
Créer un fichier guerrier.py qui décrit une classe Guerrier qui hérite de Personnage et qui à une méthode en plus : attaquePuissante.
attaquePuissante fonctionne comme attaquer, mais elle inflige 1,5 fois les dégâts de l’arme.

Méthode attaquePuissante.

Entrée : Cible (Personnage)
Sortie : -rien-
Appelle la méthode recevoirDegats du personnage reçu en paramètre (avec self.degatsArme * 1,5
en paramètre)
Attention, attaquePuissante doit faire des dégâts entier

- Magicien

Pour les magos, c'est plus compliqué … forcément ! Une des différence entre un magicien et un personnage : à la création, les magiciens ont 100 points de mana.
2eme différence : Les magicien ont un sort de méditation qui leur redonne 40 point de mana (maximum 100).
Créer un fichier magicien.py qui décrit une classe Magicien qui hérite de Personnage.
Méthode mediter
Entrée : -rien-
Sortie : -rien-
Augmente le mana de 40 ; maximum = 100

- Magicien rouge / Magicien Blanc

Il y a 2 écoles de magie !
La magie blanche (ils lancent des sorts de soin).
La magie rouge (ils lancent des boules de feu).
Votre magicien doit donc se spécialiser !
Et pour ça … on vas faire des héritages d'héritages !
La classe MageBlanc va hériter de Magicien et ajouter la méthode soigner.
Cette méthode double les points de vie (max. 100) de la cible et coûte 35 points de mana au lanceur.
Si il n'a pas assez de mana, le sort ne fait rien.
La classe MageRouge va hériter de Magicien et ajouter la méthode boulleDeFeu.
Ce sort fait 60 de dégâts à la cible et coûte 65 points de mana au lanceur.
Si il n'a pas assez de mana, le sort ne fait rien.
A faire : Implémenter les classes MageBlanc et MageRouge dans magicien.py.

Étape 5 :

Modifiez le fichier RPG.py pour que le joueur choisisse, en plus de son nom, son personnage :

Étape 1 bis : Vous êtes ...

1 - un guerrier (100 points de vie, attaque puissante)
2 - un mage rouge (120 pv, boule de feu)
3 - un mage blanc (120 pv, sort de soin)
0 – Quitter le jeu

Modifiez aussi la « boucle de combat » pour que le jeu propose les actions spéciales de la classe du joueur :

Ex (Si je joue un mage rouge)

1 - Attaquer
2- Changer d'arme (Épée, 40 dg)
3 - Méditer (+ 40 mana)
4 – Lancer une boule de feu
0 - Abandonner

Règle : Chaque action (Changer d’arme, méditer, lancer un sort, …) laissent le temps au monstre de vous attaquer une fois.
Important : Votre menu doit être construit dynamiquement en fonction de la classe du joueur et ne pas afficher les actions des autres classes (pas d’attaque puissante pour les magos … )

### 💻 Applications et langages utilisés :

+ Python
+ Atom




## 🌸 Merci !
© J-IFT
