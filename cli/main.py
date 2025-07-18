from animals.Lion import Lion
from animals.Snake import Snake
from zoo.Zoo import Zoo, animal_list

z = Zoo()

l = Lion('l001', 'Oscar', 12, 150, 20, 80, 30, 'alpha', 110)
z.add_animal(l)
s = Snake('S001', 'Jack', 3, 7, 'True', 200, 'striped', 'yellow', 25)
z.add_animal(s)

print (animal_list)