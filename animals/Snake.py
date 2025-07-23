from .Animal import Animal

class Snake(Animal):
    def __init__(self, unique_id, name, age, weight, is_venomous, body_length, skin_pattern, skin_color, average_lifespan):
        super().__init__(unique_id, name, age, weight)
        self.is_venomous = is_venomous
        self.body_length = body_length
        self.skin_pattern = skin_pattern
        self.skin_color = skin_color
        self.average_lifespan = average_lifespan
    
    def make_sound(self):
        return 'Hissssss'
    def eat(self):
        return 'Snake is seating rabbits'
    def sleep(self):
        return "it sleeps at 5PM"
    def info(self):
        return(
            f"the animal unique_id is: {self.unique_id}\n"
            f"the animal name is: {self.name}\n"
            f"the animal age is: {self.age}\n"
            f"the animal weight is: {self.weight}\n"
            f"the animal is_venomous is: {self.is_venomous}\n"
            f"the animal body_length is: {self.body_length}\n"
            f"the animal skin_pattern is: {self.skin_pattern}\n"
            f"the animal skin_color is: {self.skin_color}\n"
            f"the animal average_lifespan is: {self.average_lifespan}\n"
        )
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
            f"Is Venomous: {self.is_venomous}\n"
            f"Body Length: {self.body_length}\n"
            f"Skin Pattern: {self.skin_pattern}\n"
            f"Skin Color: {self.skin_color}\n"
            f"Average Lifespan: {self.average_lifespan}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(unique_id='{self.unique_id}', name='{self.name}', "
            f"age={self.age}, weight={self.weight}, is_venomous={self.is_venomous}, "
            f"body_length={self.body_length}, skin_pattern={self.skin_pattern}, "
            f"skin_color='{self.skin_color}', average_lifespan={self.average_lifespan})"
        )

    def make_dict(self):
        return {
        "type": self.__class__.__name__,
        "unique_id": self.unique_id,
        "name": self.name,
        "age": self.age,
        "weight": self.weight,
        "is_venomous": self.is_venomous,
        "body_length": self.body_length,
        "skin_pattern": self.skin_pattern,
        "skin_color": self.skin_color,
        "average_lifespan": self.average_lifespan,         
        }

    @classmethod
    def from_dict(cls, data: dict):
        s = Snake(data["unique_id"],
                      data["name"],
                        data["age"],
                          data["weight"],
                            data["is_venomous"],
                              data["body_length"],
                                data["skin_pattern"],
                                  data["skin_color"],
                                    data["average_lifespan"])
        return s

# s = Snake('S001', 'Jack', 3, 7, 'True', 200, 'striped', 'yellow', 25)
# s.info()
# s.perform_daily_routine()