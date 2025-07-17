from Animal import Animal

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
            f"Mane Size: {self.mane_size}\n"
            f"Tail Size: {self.tail_size}\n"
            f"Roar Volume: {self.roar_volume}\n"
            f"Group Rank: {self.group_rank}\n"
            f"Speed: {self.speed}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(unique_id='{self.unique_id}', name='{self.name}', "
            f"age={self.age}, weight={self.weight}, mane_size={self.mane_size}, "
            f"tail_size={self.tail_size}, roar_volume={self.roar_volume}, "
            f"group_rank='{self.group_rank}', speed={self.speed})"
        )


l = Lion('l001', 'Oscar', 12, 150, 20, 80, 30, 'alpha', 110)
l.info()
l.perform_daily_routine()
# print (l.unique_id)
# print (l.name)
# print(l.age)
# l.age = 18
# print(l.age)
# print(l.weight)