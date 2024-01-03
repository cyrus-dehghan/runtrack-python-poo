from math import *
class Cercle():
    def __init__(self,rayon):
        self.rayon=rayon
    
    def ChangerRayon(self,new):
        self.rayon=new
        print ("Le rayon à été modifié")

    def diametre(self):
        return self.rayon*2
    
    def circonférence(self):
        return self.diametre() * pi
    
    def aire(self):
        return pi * (self.rayon*self.rayon)

    def afficherInfos(self):
        print ("Le rayon du cercle est de",self.rayon)
        print ("La circonférence du cercle est de",round(self.circonférence(),4))
        print ("L'aire du cercle est de",round(self.aire(),4))
        print ("Le diametre du cercle est de",self.diametre())
    
job08=Cercle(4)
job08.afficherInfos()
job08.ChangerRayon(7)
job08.afficherInfos()