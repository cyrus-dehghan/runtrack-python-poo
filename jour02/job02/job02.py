class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages

mon_livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 722)

print("Titre:", mon_livre.get_titre())
print("Auteur:", mon_livre.get_auteur())
print("Nombre de pages:", mon_livre.get_nombre_pages())

mon_livre.set_titre("Harry Potter")
mon_livre.set_auteur("J.K. Rowling")
mon_livre.set_nombre_pages(320)
mon_livre.set_nombre_pages(-100)  

print("\nNouveau titre:", mon_livre.get_titre())
print("Nouvel auteur:", mon_livre.get_auteur())
print("Nouveau nombre de pages:", mon_livre.get_nombre_pages())