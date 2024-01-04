import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        adversaire.vie -= degats
        print(f"Le {self.nom} attaque l'{adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))
        if niveau in [1, 2, 3]:
            self.niveau = niveau
        else:
            print("Niveau invalide. Niveau par défaut : 1.")

    def lancerJeu(self):
        joueur = Personnage("Joueur", self.niveau * 10)
        ennemi = Personnage("Ennemi", self.niveau * 10)

        print(f"Un ennemi redoutable apparaît ! Niveau de difficulté : {self.niveau}")
        print(f"Le {joueur.nom} a {joueur.vie} points de vie.")
        print(f"L'{ennemi.nom} a {ennemi.vie} points de vie.")

        while joueur.vie > 0 and ennemi.vie > 0:
            input("Appuyez sur Entrée pour attaquer...")
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"l'{ennemi.nom} a été vaincu ! Félicitations, vous avez gagné!")
                break
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"le {joueur.nom} a été vaincu. Game over!")
                break
            print(f"Le {joueur.nom} a {joueur.vie} points de vie restants.")
            print(f"L'{ennemi.nom} a {ennemi.vie} points de vie restants.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.choisirNiveau()
    jeu.lancerJeu()