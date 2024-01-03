class Operation():
    nombre1=12
    nombre2=3
    opp=0
    
    def afficher(self):
        print("Le nombre1 est ", self.nombre1)
        print("Le nombre2 est ", self.nombre2)
    
    def addition(self):
        self.opp=self.nombre1+self.nombre2
        print (self.opp)

job03=Operation()
job03.addition()