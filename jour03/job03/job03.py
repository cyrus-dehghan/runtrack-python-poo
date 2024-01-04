class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut : {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")

    def supprimerTache(self, titre):
        tache_a_supprimer = None
        for tache in self.taches:
            if tache.titre == titre:
                tache_a_supprimer = tache
                break

        if tache_a_supprimer:
            self.taches.remove(tache_a_supprimer)
            print(f"Tâche '{titre}' supprimée de la liste.")
        else:
            print(f"Tâche '{titre}' introuvable dans la liste.")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                print(f"Tâche '{titre}' marquée comme terminée.")
                break
        else:
            print(f"Tâche '{titre}' introuvable dans la liste.")

    def afficherListe(self):
        print("Liste des tâches :")
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        taches_filtrees = [tache for tache in self.taches if tache.statut == statut]
        print(f"Tâches avec le statut '{statut}' :")
        for tache in taches_filtrees:
            print(tache)


tache1 = Tache("Faire les courses", "Acheter des fruits")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 7", "À faire")
tache3 = Tache("Nettoyer la maison", "Laver les vêtements")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

liste_taches.afficherListe()

liste_taches.marquerCommeFinie("Faire les courses")

liste_taches.filterListe("À faire")

liste_taches.supprimerTache("Réviser pour l'examen")

liste_taches.afficherListe()
