
from model.interface import *

class SmallStudent(Person,Student):

    """
       student entity class
    """
    def __init__(self,name,age,*args,**kwargs):
        Person.__init__(self,name,age,1)
        Student.__init__(self,"1")

    def __hash__(self):
        return super.__hash__(self)

    def __str__(self):
        return self._name+"a"