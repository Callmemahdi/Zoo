from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, Unique_id, Name, Age, Weight):
        self.__unique_id = Unique_id
        self.__name = Name
        self.__age = Age
        self.__weight = Weight

    @property
    def unique_id(self):
        return self.__unique_id
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            raise ValueError("the age must be positive")
        
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value >= 0:
            self.__weight = value
        else:
            raise ValueError("the weight must be positive")

    @abstractmethod
    def eat(sleep):
        pass
    
    @abstractmethod
    def sleep(sleep):
        pass

    @abstractmethod
    def make_sound(self):
        pass
