from animals.Lion import Lion
from zoo.Zoo import Zoo, animal_list

z = Zoo()

l = Lion('l001', 'Oscar', 12, 150, 20, 80, 30, 'alpha', 110)
z.add_animal(l)
print (animal_list)