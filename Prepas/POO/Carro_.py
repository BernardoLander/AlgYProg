class Car():

    def __init__(self, mark, driver):

        self.mark=mark
        self.driver=driver
        self.position=-1
    
    def get_mark(self):
        return self.mark

    def get_driver(self):
        return self.driver

    def set_mark(self,new_mark):
        self.mark=new_mark

    def set_driver(self,new_driver):
        self.driver=new_driver

    def get_position(self):
        return self.position
    
    def set_position(self,new_position):
        self.position=new_position
    



