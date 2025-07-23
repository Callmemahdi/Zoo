from .Animal import Animal
class Elephant(Animal):
    def __init__(self, unique_id: str, name: str, age: int, weight: float, body_length: float, tusk_length: float, species: str, habitat: str, lifespan: int) -> None:
        super().__init__(unique_id, name, age, weight)
        self.body_length: float  = body_length
        self.tusk_length: float = tusk_length
        self.species: str = species
        self.habitat: str = habitat
        self.lifespan: int = lifespan

    def make_sound(self) -> str:
        return 'Pawooooo'
    def eat(self) -> str:
        return 'Elephant is eating vegetables'
    def sleep(self) -> str:
        return 'Elephant is sleeping at 9AM'
    def info(self) -> str:
        info_str = (
            f"the animal unique_id is: {self.unique_id}\n"
            f"the animal name is: {self.name}\n"
            f"the animal age is: {self.age}\n"
            f"the animal weight is: {self.weight}\n"
            f"the animal body_length is: {self.body_length}\n"
            f"the animal tusk_length is: {self.tusk_length}\n"
            f"the animal species is: {self.species}\n"
            f"the animal habitat is: {self.habitat}\n"
            f"the animal lifespan is: {self.lifespan}\n"
        )
        return info_str  

    def perform_daily_routine(self) -> None:
        self.make_sound()
        self.eat()
        self.sleep()
    
    def __str__(self) -> str:
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

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(unique_id='{self.unique_id}', name='{self.name}', "
            f"age={self.age}, weight={self.weight},body_length={self.body_length},"
            f"tusk_length={self.tusk_length}, species={self.species}, "
            f"habitat='{self.habitat}', lifespan={self.lifespan}"
            )

    def make_dict(self) -> dict[str, str | int | float]:
        return {
        "type": self.__class__.__name__,
        "unique_id": self.unique_id,
        "name": self.name,
        "age": self.age,
        "weight": self.weight,
        "body_length": self.body_length,
        "tusk_length": self.tusk_length,
        "species": self.species,
        "habitat": self.habitat,
        "lifespan": self.lifespan,         
        }
    @classmethod
    def from_dict(cls, data: dict[str, str | int | float]) -> "Elephant":
        e = Elephant(data["unique_id"],
                    data["name"],
                    data["age"],
                    data["weight"],
                    data["body_length"],
                    data["tusk_length"],
                    data["species"],
                    data["habitat"],
                    data["lifespan"])
        return e
# e = Elephant('E001', 'Horton', 11, 3500, 450, 250, 'Asian', 'jungle', 43,)
# e.info()
# e.perform_daily_routine()