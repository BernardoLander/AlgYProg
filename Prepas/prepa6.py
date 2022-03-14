#6 carros y random 

class car():
    #Constructor
    def __init__(self, brand, driver):
        self.__carBrand = brand
        self.__carDriver = driver
        self.__position = -1

    #Getters
    def getDriver(self):
        return self.__carDriver
    
    def getBrand(self):
        return self.__carBrand
    
    def getPosition(self):
        return self.__position
    
    #Setters

    def setPosition (self, newPosition):
        self.__position = newPosition

    def setBrand (self,newBrand):
        self.__carBrand = newBrand
    
    def setDriver (self, newDriver):
        self.__carDriver = newDriver