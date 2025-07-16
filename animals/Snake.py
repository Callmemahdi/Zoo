from Animal import Animal

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

    def perform_daily_routine(self):
        self.make_sound()
        self.eat()
        self.sleep()

s = Snake('S001', 'Jack', 3, 7, 'True', 200, 'striped', 'yellow', 25)
s.info()
s.perform_daily_routine()