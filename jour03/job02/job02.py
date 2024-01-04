class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde} €")
        print(f"Autorisation de découvert : {self.__decouvert}")

    def afficherSolde(self):
        print(f"Solde du client {self.__nom} {self.__prenom} : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Opération impossible : solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios de {agios} € appliqués. Nouveau solde : {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Opération impossible : solde insuffisant.")


compte1 = CompteBancaire("12345", "Lebron", "James", 1000)

compte1.afficher()

compte1.versement(150)

compte1.retrait(20)

compte1.afficherSolde()

compte2 = CompteBancaire("67890", "Michael", "Jordan", -500, decouvert=True)

compte2.agios(0.05)  

compte2.afficher()

compte1.virement(compte2, 30)

compte1.afficherSolde()
compte2.afficherSolde()