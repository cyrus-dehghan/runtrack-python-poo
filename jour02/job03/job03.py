class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible a l'emprunt.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre est déjà disponible.")

mon_livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 722)

print("Le livre est disponible :", mon_livre.verification())

mon_livre.emprunter()

mon_livre.emprunter()

mon_livre.rendre()

mon_livre.rendre()

print("Le livre est à nouveau disponible :", mon_livre.verification())