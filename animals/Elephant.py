from .Animal import Animal
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

    def perform_daily_routine(self):
        self.make_sound()
        self.eat()
        self.sleep()
    
    def __str__(self):
        return (
            f"{self.__class__.__name__}:\n"
            f"ID: {self.unique_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Weight: {self.weight}\n"
            f"Body Length: {self.body_length}\n"
            f"Tusk Length: {self.tusk_length}\n"
            f"Species: {self.species}\n"
            f"Habitat: {self.habitat}\n"
            f"Lifespan: {self.lifespan}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(unique_id='{self.unique_id}', name='{self.name}', "
            f"age={self.age}, weight={self.weight},body_length={self.body_length},"
            f"tusk_length={self.tusk_length}, species={self.species}, "
            f"habitat='{self.habitat}', lifespan={self.lifespan}"
            )

e = Elephant('E001', 'Horton', 11, 3500, 450, 250, 'Asian', 'jungle', 43,)
e.info()
e.perform_daily_routine()