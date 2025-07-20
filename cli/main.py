from animals.Lion import Lion
from animals.Snake import Snake
from animals.Elephant import Elephant

from zoo.Zoo import Zoo, animal_list
from storage.json_storage import JsonStorage
# z = Zoo()
# s = JsonStorage()

# l = Lion('l001', 'Oscar', 12, 150, 20, 80, 30, 'alpha', 110)
# z.add_animal(l)
# s.save(l)

# l = Lion('l002', 'Rex', 13, 140, 18, 84, 20, 'beta', 120)
# z.add_animal(l)

# s = Snake('S001', 'Jack', 3, 7, 'True', 200, 'striped', 'yellow', 25)
# z.add_animal(s)
#print (animal_list)

# z.remove_animal('S001')
#print (animal_list)
#z.show_animals()

#z.serach_animal_by_name('Oscar')
# z.search_animal_by_id('S001')
#print (animal_list[1].name)

# z.count_by_type('Lion')
# z.count_by_type('Snake')
# z.count_all_animals()
print('Welcome to the zoo')
my_zoo = Zoo()
my_json = JsonStorage()
my_csv = None
my_db = None
def show_menu():
    print('Plese select the service:\n1- Add an animal\n2- Show all animals\n3- delete an animal\n4- Search the animal by name\n5- Search the animal by id\n6- Show count of animals of a specific type\n7- Show count of all animals')
    n =input()
    if n == '1':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print('Please enter the animal type:\n1- Lion\n2-Snake\n3-Elephant')
            i = input()
            if i == '1':
                print('Please enter the details of the desired animal')
                print('unique_id:')
                unique_id = input()
                print('name:')
                name = input()
                print('age:')
                age = input()
                print('weight:')
                weight = input()
                print('mane_size:')
                mane_size = input()
                print('tail_size:')
                tail_size = input()
                print('roar_volume:')
                roar_volume = input()
                print('group_rank:')
                group_rank = input()
                print('speed:')
                speed = input()
                l = Lion(unique_id, name, age, weight, mane_size, tail_size, roar_volume, group_rank, speed)
                my_zoo.add_animal_json(l, my_json)

            if i == '2':
                print('Please enter the details of the desired animal')
                print('unique_id:')
                unique_id = input()
                print('name:')
                name = input()
                print('age:')
                age = input()
                print('weight:')
                weight = input()
                print('is_venomous:')
                is_venomous = input()
                print('body_length:')
                body_length = input()
                print('skin_pattern:')
                skin_pattern = input()
                print('skin_color:')
                skin_color = input()
                print('average_lifespan:')
                average_lifespan = input()
                l = Snake(unique_id, name, age, weight, is_venomous, body_length, skin_pattern, skin_color, average_lifespan)
                my_zoo.add_animal_json(l, my_json)
            if i == '3':
                print('Please enter the details of the desired animal')
                print('unique_id:')
                unique_id = input()
                print('name:')
                name = input()
                print('age:')
                age = input()
                print('weight:')
                weight = input()
                print('body_length:')
                body_length = input()
                print('tusk_length:')
                tusk_length = input()
                print('species:')
                species = input()
                print('habitat:')
                habitat = input()
                print('lifespan:')
                lifespan = input()
                l = Elephant(unique_id, name, age, weight, body_length, tusk_length, species, habitat, lifespan)
                my_zoo.add_animal_json(l, my_json)
        if i == '2':
            pass
        if i == '3':
            pass
    elif n == '2':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            my_zoo.show_animals_json(my_json)
        if i == '2':
            pass
        if i == '3':
            pass
    elif n == '3':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print("enter the animal's ID:")
            i = input()
            my_json.delete(i)
        if i == '2':
            pass
        if i == '3':
            pass
    elif n == '4':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print("Enter the animal's name:")
            i = input()
            print(my_json.search_by_name(i))
        if i == '2':
            pass
        if i == '3':
            pass
    elif n == '5':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print("Enter the animal's ID")
            i = input()
            print(my_json.search_by_id(i))
        if i == '2':
            pass
        if i == '3':
            pass
    elif n == '6':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print("enter the animal type:")
            i = input()
            if i == "Lion" or i == "Snake" or i == "Elephant":
                print(my_json.count_by_type(i))
            else:
                print("this animal type isn't exist in zoo")
        if i == '2':
            pass
        if i == '3':
            pass
    elif n == '7':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            pass
        if i == '2':
            pass
        if i == '3':
            pass

    else:
        print('please just type a number from 1 to 7')

show_menu()