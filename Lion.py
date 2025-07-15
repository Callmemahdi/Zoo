from . Zoo import Animal

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