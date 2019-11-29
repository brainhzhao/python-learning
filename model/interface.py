
#-*- coding:utf-8 -*-

__author__="zhaoheng"
__version__="1.0"

class Person:

    __doc__ = """
        base person
    """

    def __init__(self,name,age,sex):
        self._name=name
        self._age=age
        self._sex=sex
        print("init person")

    def sayHello(self):
        raise RuntimeError("方法没有实现")


class Student():

    def __init__(self,className):
        self.__class=className
        print("init student")

    def sayClass(self):
        raise RuntimeError("This method not implement")

stu_test=Student('2')