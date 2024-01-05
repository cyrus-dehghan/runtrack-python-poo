class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

rectangle = Rectangle(largeur=5, hauteur=3)

resultat_aire_rectangle = rectangle.aire()

print("L'aire du rectangle est:", resultat_aire_rectangle)