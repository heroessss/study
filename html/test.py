class Person:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name + 'sb'
    @name.setter
    def name(self,new_name):
        self.__name = new_name