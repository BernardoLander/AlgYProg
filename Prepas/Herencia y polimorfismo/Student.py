from Persona import *
class Student(Persona):

    def __init__(self, name, last_name, id, carnet):

        Persona.__init__(self,name,last_name,id)

        self.__carnet=carnet
        self.__subjects=[]
    
    
    def get_carnet(self):
        return self.__carnet
        
    def set_carnet(self,new_carnet):
        self.__carnet=new_carnet
    
    def get_subjects(self):
        return self.__subjects

    def set_subjects(self, new_subjects):
        self.__subjects = new_subjects

    
