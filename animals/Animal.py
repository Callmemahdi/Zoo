from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, Unique_id, Name, Age, Weight)-> None:
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


    def __str__(self)-> str:
        return (
            f"{self.__class__.__name__}:\n"
            f"  ID: {self.unique_id}\n"
            f"  Name: {self.name}\n"
            f"  Age: {self.age}\n"
            f"  Weight: {self.weight}"
        )   

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(unique_id='{self.unique_id}', "
            f"name='{self.name}', age={self.age}, weight={self.weight})"
        )
    
    @abstractmethod
    def eat(self) -> str:
        pass
    
    @abstractmethod
    def sleep(self) -> str:
        pass

    @abstractmethod
    def make_sound(self) -> str:
        pass

    
    @abstractmethod
    def perform_daily_routine(self)-> str:
        pass