class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def augmenter_population(self):
        self.__nombre_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_population(self):
        self.__ville.augmenter_population()

paris = Ville("Paris", 1000000)
print(f"Population de la ville de {paris.get_nom()} : {paris.get_nombre_habitants()}")

marseille = Ville("Marseille", 861635)
print(f"Population de la ville de {marseille.get_nom()} : {marseille.get_nombre_habitants()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

print(f"Mise à jour de la population de la ville de {paris.get_nom()}: {paris.get_nombre_habitants()}")
print(f"Mise à jour de la population de la ville de {marseille.get_nom()}: {marseille.get_nombre_habitants()}")
