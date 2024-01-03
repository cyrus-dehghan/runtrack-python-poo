class point():

    def __init__(self,x, y):
        self.x=x
        self.y=y
    
    def afficherLesPoints(self):
        print ("Les coordonnées du point est",self.x,self.y)
    
    def afficherX(self):
        print ("Le point a pour x",self.x)

    def afficherY(self):
        print ("Le point a pour y",self.y)
    
    def changerX(self,new):
        self.x=new
        print ("x a changé")
    
    def changerY(self,new):
        self.y=new
        print ("y a changé")
    
job05=point(20,25)
job05.afficherLesPoints()
job05.changerX(25)
job05.changerY(30)
job05.afficherX()
job05.afficherY()
