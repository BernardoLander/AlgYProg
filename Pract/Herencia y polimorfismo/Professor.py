from Persona import *
class Professor(Persona):

    def __init__(self,name,last_name,id,materia):

        Persona.__init__(self,name,last_name,id)
        
        
        self.__materia=materia #EN ESTE CASO SUPONGAMOS QUE UN PROFESOR SOLO PUEDE DAR UNA SOLA MATERIA
        self.__secciones=[]    #Y QUE DE ESA MATERIA PUEDE DAR VARIAS ASIGNATURAS


    def get_materia(self):
        return self.__materia

    def set_secciones(self,new_secciones):
        self.__secciones = new_secciones
    
    def get_secciones(self):
        return self.__secciones
        
    def add_secciones(self,section):
        
        self.__secciones.append(section)
        return self.__secciones
        
        
