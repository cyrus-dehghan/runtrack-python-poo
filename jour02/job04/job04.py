class Student():

    def __init__(self, nom, prenom, num):
        self.__nom = nom
        self.__prenom = prenom
        self.__num = num
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self,nb):
        if nb > 0 :
            self.__credits+=nb
            self.__level = self.__studentEval()
        else:
            print ("Le nombre de crédits doit être superieur à 0")
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_num(self):
        return self.__num

    def get_credits(self):
        return self.__credits
    
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >=70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else :
            return "Insuffisant"
        
    def get_level(self):
        return self.__level
        
    def studentInfo(self):
        print ("Nom =",self.get_nom())
        print ("Prénom =",self.get_prenom())
        print ("id =",self.get_num())
        print ("Niveau =",self.get_level())

john = Student("John","Doe",145)
john.add_credits(10)
john.add_credits(10)
john.add_credits(10)
print ("Le nombre de crédits de",john.get_prenom(),john.get_nom(),"est de",john.get_credits(),"points.")
john.add_credits(45)
john.studentInfo()