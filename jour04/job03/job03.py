class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, value):
        if value > 0:
            self._longueur = value
        else:
            print("La longueur doit être un nombre positif.")

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, value):
        if value > 0:
            self._largeur = value
        else:
            print("La largeur doit être un nombre positif.")

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, value):
        if value > 0:
            self._hauteur = value
        else:
            print("La hauteur doit être un nombre positif.")

    def volume(self):
        return self._longueur * self._largeur * self._hauteur


rectangle = Rectangle(longueur=5, largeur=3)

print("Longueur:", rectangle.longueur)
print("Largeur:", rectangle.largeur)
print("Périmètre:", rectangle.perimetre())
print("Surface:", rectangle.surface())

rectangle.longueur = 8
rectangle.largeur = 4

print("Nouvelle longueur:", rectangle.longueur)
print("Nouvelle largeur:", rectangle.largeur)
print("Nouveau périmètre:", rectangle.perimetre())
print("Nouvelle surface:", rectangle.surface())

parallelepipede = Parallelepipede(longueur=3, largeur=2, hauteur=4)

print("Volume du parallélépipède:", parallelepipede.volume())