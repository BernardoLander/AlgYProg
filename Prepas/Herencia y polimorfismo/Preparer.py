
from Professor import *
from Student import *

class Preparer(Student,Professor):

    def __init__(self,name,last_name,id,carnet,materia):

        Professor.__init__(self,name,last_name,id,materia)
        Student.__init__(self, name,last_name,id,carnet)

    