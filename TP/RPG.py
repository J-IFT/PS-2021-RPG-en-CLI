""" Étape 3 : RPG.py
Écrire un fichier RPG.py qui permet d’utiliser la classe de personnage dans un micro-jeu-de-roleen-
ligne-de-commande-pour-les-nuls.
Étape 3.1 : Demander au joueur le nom de son personnage
Instancier un objet de la classe Personnage avec 120 points de vie.
Étape 3.2 : Demander dans un menu qui l’on veut combattre
1 - un gobelin (75 pv, armé d’un gourdin (15 dg))
2 - un orc (100 pv, armé d’une épée rouillée (20 dg))
3 - un troll (200 pv, armé d’une hache (30 dg))
0 – Quitter le jeu
Attention, votre code doit être « résistant aux erreurs de saisie » et n’accepter que les choix 0 ~ 3
Étape 3.3 - Puis boucler sur un second menu qui
– Affiche le statut de chacun des 2 personnages
– Demande au joueur de choisir entre
1 - Attaquer
2 - Changer d'arme (Épée, 45 dg)
0 - Abandonner
Arrêtez quand (au moins) l'un des 2 est mort
Affichez le vainqueur
Retourner à l’étape 2
Règle : Si Le joueur change d’arme l’adversaire l’attaque une fois « gratuitement »
Règle : Abandon = défaite ; match nul = défaite2
Attention : Votre jeu doit être « résistant à une erreur de saisie ». """

""" Étape 5
Modifiez le fichier RPG.py pour que le joueur choisisse, en plus de son nom, son personnage :
Étape 1 bis : Vous êtes ...
1 - un guerrier (100 points de vie, attaque puissante)
2 - un mage rouge (120 pv, boule de feu)
3 - un mage blanc (120 pv, sort de soin)
0 – Quitter le jeu
Modifiez aussi la « boucle de combat » pour que le jeu propose les actions spéciales de la classe du
joueur :
Ex (Si je joue un mage rouge)
1 - Attaquer
2- Changer d'arme (Épée, 40 dg)
3 - Méditer (+ 40 mana)
4 – Lancer une boule de feu
0 - Abandonner
Règle : Chaque action (Changer d’arme, méditer, lancer un sort, …) laissent le temps au monstre de
vous attaquer une fois.
Important : Votre menu doit être construit dynamiquement en fonction de la classe du joueur et ne
pas afficher les actions des autres classes (pas d’attaque puissante pour les magos … ) """

## Je lie les fichiers ensemble grâce à from/import.
from personnage import Personnage
from arme import Arme
from guerrier import Guerrier
from magicien import Magicien, MageBlanc, MageRouge
## Je passe à l'étape 3.2 pour la création du menu pour demander qui il veut combattre tout en suivant l'énoncé :
def menu():
    print("1 - Un gobelin (75 pv, armé d’un gourdin (15 dg))")
    print("2 - Un orc (100 pv, armé d’une épée rouillée (20 dg))")
    print("3 - Un troll (200 pv, armé d’une hache (30 dg))")
    print("0 – Quitter le jeu \n")
## Je m'occupe de l'étape 5 et je créé le menu correspondant aux classes.
def menuclasses():
    print("1 - Un guerrier (100 points de vie, attaque puissante)")
    print("2 - Un mage rouge (120 pv, boule de feu)")
    print("3 - Un mage blanc (120 pv, sort de soin)")
    print("0 – Quitter le jeu \n")

## Comme demandé dans l'étape 3.1 je demande au joueur le nom du personnage et je l'instancie à 120 points de vie.
## (pour l'étape de la fin je dois modifier un peu tout donc certains commentaires ne sont plus valables.)
## Je lui souhaite également la bienvenue avec une petite référence à League of Legends (ce n'est pas un placement de produit même si j'aimerai bien)
nom=input("Quel est le nom du personnage ? \n")
print("Bienvenue dans la faille de l'invocateur, {} \n".format(nom))
menuclasses()
try:
    choix=(int(input("Choisissez votre classe : \n")))
    if 0<=choix<=3:
        if choix==1:
            joueur=Guerrier(nom,vie=100)
        elif choix==2:
            joueur=MageRouge(nom,vie=120)
        elif choix==3:
            joueur=MageBlanc(nom,vie=120)
        elif choix==0:
            print("Un invocateur a quitté la partie !\n")
            exit()
        else:
            print("La classe choisie est : {} \n".format(joueur.getNom()))
    else:
        print("Choisir uniquement 1, 2, 3 ou 0 : veuillez recommencer.\n")
except ValueError:
    print("Veuillez entrer un entier. \n")

pvmax=joueur.getPv()
manamax=joueur.getMana()
armechange=joueur.getArme()
classe=joueur.__class__.__name__

while True:
## Je m'occupe de l'action qui sera effectuée lorsqu'il fera son choix.
## Je me suis permise un peu de personnalisation...(j'aurais pû mettre le prénom de certains de mes camardes finalement)
## Au cas où (je ne doute pas de votre culture geek) : Krenko (magic the gathering), Thrall (world of warcraft), Trundle (league of legends)
    while True:
        menu()
        try:
            choix=(int(input("Choisissez un adversaire : \n")))
            if 0<=choix<=3:
                if choix==1:
                    adversaire=Personnage("Krenko (gobelin)",vie=75,mana=0,nomArme="gourdin",dgArme=15)
                    break
                elif choix==2:
                    adversaire=Personnage("Thrall (orc)",vie=100,mana=0,nomArme="épée rouillée",dgArme=20)
                    break
                elif choix==3:
                    adversaire=Personnage("Trundle (troll)",vie=200,mana=0,nomArme="hache",dgArme=30)
                    break
                elif choix==0:
                    print("Un invocateur a quitté la partie !\n")
                    exit()
                else:
                    print("L'adversaire choisi est : {} \n".format(adversaire.getNom()))
                    break
            else:
                print("Choisir uniquement 1, 2, 3 ou 0 : veuillez recommencer.\n")
        except ValueError:
            print("Veuillez entrer un entier. \n")
## Je me sers de try/except pour empêcher les erreurs de saisie comme par exemple entrer des lettres au lieu des chiffres.
## Je passe à l'étape 3 où il faut boucler le second menu, toujours en suivant l'énoncé tout en essayant de suivre les règles imposées.
    round=1
    while(joueur.estVivant() and adversaire.estVivant()):
        print("~~~~~~~~~~ ROUND",str(round),"~~~~~~~~~~\n")
        print(joueur)
        print(adversaire)
        print("1 - Attaquer")
        print("2 - Changer d'arme (Épée, 45 dg)")
        if classe=="Guerrier":
            print("3 - Attaque puissante")
        elif classe=="MageRouge":
            print("3 - Méditer (+ 40 mana)")
            print("4 – Lancer une boule de feu")
        elif classe=="MageBlanc":
            print("3 - Méditer (+ 40 mana)")
            print("4 – Lancer un sort de soin")
        print("0 - Abandonner \n")
        try:
            action=int(input("Que voulez-vous faire, invocateur ?\n"))
            if action==1:
                joueur.attaquer(adversaire)
            elif action==2:
                joueur.changerArme("Épée",45)
            elif action==3 and classe=="Guerrier":
                joueur.attaquePuissante(adversaire)
            elif action==3 and classe=="MageRouge":
                joueur.mediter()
            elif action==4 and classe=="MageRouge":
                joueur.boulleDeFeu(adversaire)
            elif action==3 and classe=="MageBlanc":
                joueur.mediter()
            elif action==4 and classe=="MageBlanc":
                joueur.soigner(joueur)
            elif action==0:
                print("Vous avez abandonné le combat, retour à la base.\n")
                break
        except ValueError:
            print("Choisir uniquement 1, 2, 3 ou 0 : veuillez recommencer.\n")
        adversaire.attaquer(joueur)
        round+=1
## J'ajoute des prints pour la mise en forme et la clarté du jeu.
    if (not(joueur.estVivant()) and not(adversaire.estVivant())):
        print("Retour à la base pour vous deux !\n")
        joueur.setPv(pvmax)
        joueur.setMana(manamax)
        
    elif (not(joueur.estVivant())):
        print("Retour à la base : vous avez perdu le combat.\n")
        joueur.setPv(pvmax)
        joueur.setMana(manamax)

    elif joueur.estVivant() and not(adversaire.estVivant()):
        print("Vous avez gagné le combat ! \n")
        joueur.setPv(pvmax)
        joueur.setMana(manamax)
