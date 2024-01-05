import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def initialiser_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        return paquet

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

    def distribuer_cartes(self):
        self.main_joueur = [self.tirer_carte(), self.tirer_carte()]
        self.main_croupier = [self.tirer_carte(), self.tirer_carte()]

    def calculer_points(self, main):
        total_points = 0
        as_present = False

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total_points += 10
            elif carte.valeur == 'As':
                as_present = True
                total_points += 1
            else:
                total_points += int(carte.valeur)

        if as_present and total_points + 10 <= 21:
            total_points += 10

        return total_points

    def afficher_main_joueur(self):
        print("Main du joueur:")
        for carte in self.main_joueur:
            print(f"{carte.valeur} de {carte.couleur}")

    def afficher_main_croupier(self, premiere_carte=True):
        print("Main du croupier:")
        if premiere_carte:
            print(f"{self.main_croupier[0].valeur} de {self.main_croupier[0].couleur} et une carte cachée")
        else:
            for carte in self.main_croupier:
                print(f"{carte.valeur} de {carte.couleur}")

    def jouer(self):
        self.melanger_paquet()
        self.distribuer_cartes()

        while True:
            self.afficher_main_joueur()
            self.afficher_main_croupier()

            choix = input("Voulez-vous prendre une carte supplémentaire ? (Oui/Non): ").lower()

            if choix == 'oui':
                self.main_joueur.append(self.tirer_carte())
                points_joueur = self.calculer_points(self.main_joueur)

                if points_joueur > 21:
                    print("Vous avez dépassé 21 points. Vous avez perdu.")
                    return

            elif choix == 'non':
                break

        while self.calculer_points(self.main_croupier) < 17:
            self.main_croupier.append(self.tirer_carte())

        self.afficher_main_joueur()
        self.afficher_main_croupier(False)

        points_joueur = self.calculer_points(self.main_joueur)
        points_croupier = self.calculer_points(self.main_croupier)

        if points_joueur > 21 or (points_croupier <= 21 and points_croupier >= points_joueur):
            print("Le croupier gagne.")
        else:
            print("Vous gagnez.")

jeu_blackjack = Jeu()
jeu_blackjack.jouer()
