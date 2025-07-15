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


class Elephant(Animal):
    def __init__(self, unique_id, name, age, weight, body_length, tusk_length, species, habitat, lifespan):
        super().__init__(unique_id, name, age, weight)
        self.body_length = body_length
        self.tusk_length = tusk_length
        self.species = species
        self.habitat = habitat
        self.lifespan = lifespan
    
    def make_sound(self):
        print('Pawooooo')
    def eat(self):
        print('12PM')
    def sleep(self):
        print('9AM')
    def info(self):
        print(f"the animal unique_id is: {self.unique_id}")
        print(f"the animal name is: {self.name}")
        print(f"the animal age is: {self.age}")
        print(f"the animal weight is: {self.weight}")
        print(f"the animal body_length is: {self.body_length}")
        print(f"the animal tusk_length is: {self.tusk_length}")
        print(f"the animal species is: {self.species}")
        print(f"the animal habitat is: {self.habitat}")
        print(f"the animal lifespan is: {self.lifespan}")

e = Elephant('E001', 'Horton', 11, 3500, 450, 250, 'Asian', 'jungle', 43,)
e.info()