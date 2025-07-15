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


class Lion(Animal):
    def __init__(self, unique_id, name, age, weight, mane_size, tail_size, roar_volume, group_rank, speed):
        super().__init__(unique_id, name, age, weight)
        self.mane_size = mane_size
        self.tail_size = tail_size
        self.roar_volume = roar_volume
        self.group_rank = group_rank
        self.speed = speed
    
    def make_sound(self):
        print('ewww')
    def eat(self):
        print('2AM')
    def sleep(self):
        print('11AM')
    def info(self):
        print(f"the animal unique_id is: {self.unique_id}")
        print(f"the animal name is: {self.name}")
        print(f"the animal age is: {self.age}")
        print(f"the animal weight is: {self.weight}")
        print(f"the animal mane_size is: {self.mane_size}")
        print(f"the animal tail_size is: {self.tail_size}")
        print(f"the animal roar_volume is: {self.roar_volume}")
        print(f"the animal group_rank is: {self.group_rank}")
        print(f"the animal speed is: {self.speed}")

l = Lion('l001', 'Oscar', 12, 150, 20, 80, 30, 'alpha', 110)
l.info()
# print (l.unique_id)
# print (l.name)
# print(l.age)
# l.age = 18
# print(l.age)
# print(l.weight)

class Snake(Animal):
    def __init__(self, unique_id, name, age, weight, is_venomous, body_length, skin_pattern, skin_color, average_lifespan):
        super().__init__(unique_id, name, age, weight)
        self.is_venomous = is_venomous
        self.body_length = body_length
        self.skin_pattern = skin_pattern
        self.skin_color = skin_color
        self.average_lifespan = average_lifespan
    
    def make_sound(self):
        print('sssssssss')
    def eat(self):
        print('11PM')
    def sleep(self):
        print('4AM')
    def info(self):
        print(f"the animal unique_id is: {self.unique_id}")
        print(f"the animal name is: {self.name}")
        print(f"the animal age is: {self.age}")
        print(f"the animal weight is: {self.weight}")
        print(f"the animal is_venomous is: {self.is_venomous}")
        print(f"the animal body_length is: {self.body_length}")
        print(f"the animal skin_pattern is: {self.skin_pattern}")
        print(f"the animal skin_color is: {self.skin_color}")
        print(f"the animal average_lifespan is: {self.average_lifespan}")

s = Snake('S001', 'Jack', 3, 7, 'True', 200, 'striped', 'yellow', 25)
s.info()



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