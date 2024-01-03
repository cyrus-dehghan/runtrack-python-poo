class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

mon_rectangle = Rectangle(10, 5)

print("Longueur initiale:", mon_rectangle.get_longueur())
print("Largeur initiale:", mon_rectangle.get_largeur())

mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

print("\nLongueur modifiée:", mon_rectangle.get_longueur())
print("Largeur modifiée:", mon_rectangle.get_largeur())