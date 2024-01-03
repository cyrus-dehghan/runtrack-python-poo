class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  
        self.__statut_commande = "En cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
            print(f"{nom_plat} ajouté à la commande.")
        else:
            print(f"{nom_plat} est déjà dans la commande.")

    def annuler_commande(self):
        self.__plats_commandes.clear()
        self.__statut_commande = "Annulée"
        print("La commande a été annulée.")

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande}")
        for nom_plat, details_plat in self.__plats_commandes.items():
            print(f"{nom_plat}: {details_plat['prix']} € ({details_plat['statut']})")
        total = self.__calculer_total()
        print(f"Total à payer: {total} €")

    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * (taux_tva / 100)
        return tva

ma_commande = Commande("9")

ma_commande.ajouter_plat("Pizza", 10)
ma_commande.ajouter_plat("Salade", 5)
ma_commande.ajouter_plat("Pâtes", 15)

ma_commande.afficher_commande()

tva_calculée = ma_commande.calculer_tva(10)
print(f"TVA à payer: {tva_calculée} €")

ma_commande.annuler_commande()

ma_commande.afficher_commande()