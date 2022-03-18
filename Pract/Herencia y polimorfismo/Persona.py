class Persona():

    def __init__(self, name, last_name, id):
        self.__name=name
        self.__last_name=last_name
        self.__id=id


    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        self.__name = new_name
        
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self,new_last_name):
        self.__last_name=new_last_name

    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        self.__id = new_id
        
