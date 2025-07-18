from animals.Lion import Lion
from animals.Snake import Snake
from zoo.Zoo import Zoo, animal_list

z = Zoo()

l = Lion('l001', 'Oscar', 12, 150, 20, 80, 30, 'alpha', 110)
z.add_animal(l)

l = Lion('l002', 'Rex', 13, 140, 18, 84, 20, 'beta', 120)
z.add_animal(l)

s = Snake('S001', 'Jack', 3, 7, 'True', 200, 'striped', 'yellow', 25)
z.add_animal(s)
#print (animal_list)

# z.remove_animal('S001')
#print (animal_list)
#z.show_animals()

#z.serach_animal_by_name('Oscar')
z.search_animal_by_id('S001')
#print (animal_list[1].name)

z.count_by_type('Lion')
z.count_by_type('Snake')
z.count_all_animals()