from animals.Lion import Lion
from animals.Snake import Snake
from animals.Elephant import Elephant

from zoo.Zoo import Zoo
from storage.json_storage import JsonStorage
from storage.csv_storage import CsvStorage
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
print('\nWelcome to the zoo')
print ('Select your storage:\n1- JSON\n2- CSV\n3-SQL')
m = input()
if m == '1':
    storage = JsonStorage()
elif m == '2':
    storage = CsvStorage()
elif m == '3':
    pass
my_zoo = Zoo(Storage = storage)
# my_json = JsonStorage()
# my_csv = CsvStorage()
# my_db = None
def show_menu():
    print('Plese select the service:\n1- Add an animal\n2- Show all animals\n3- delete an animal\n4- Search the animal by name\n5- Search the animal by id\n6- Show count of animals of a specific type\n7- Show count of all animals')
    n =input()
    if n == '1':
            print('Please enter the animal type:\n1- Lion\n2- Snake\n3- Elephant')
            i = input()
            if i == '1':
                print('Please enter the details of the desired animal')
                lion_fields = ['unique_id', 'name', 'age', 'weight', 'mane_size', 'tail_size', 'roar_volume', 'group_rank', 'speed']
                animal_data = {}
                animal_data['type']  = 'Lion'
                for field in lion_fields:
                    animal_data[field] = input(f"Enter the animal's {field}:\n")
                my_zoo.add_animal(animal_data)                
            if i == '2':
                print('Please enter the details of the desired animal')
                lion_fields = ['unique_id', 'name', 'age', 'weight', 'is_venomous', 'body_length', 'skin_pattern', 'skin_color', 'average_lifespan']
                animal_data = {}
                animal_data['type']  = 'Snake'
                for field in lion_fields:
                    animal_data[field] = input(f"Enter the animal's {field}:\n")
                my_zoo.add_animal(animal_data)
            if i == '3':
                print('Please enter the details of the desired animal')
                lion_fields = ['unique_id', 'name', 'age', 'weight', 'body_length', 'tusk_length', 'species', 'habitat', 'lifespan']
                animal_data = {}
                animal_data['type']  = 'Elephant'
                for field in lion_fields:
                    animal_data[field] = input(f"Enter the animal's {field}:\n")
                my_zoo.add_animal(animal_data)
    elif n == '2':
       my_zoo.show_animals()
    elif n == '3':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print("enter the animal's ID:")
            i = input()
            my_zoo.remove_animal_json(i)
        if i == '2':
            print("enter the animal's ID:")
            i = input()
            my_zoo.remove_animal_csv(i)
        if i == '3':
            pass
    elif n == '4':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print("Enter the animal's name:")
            i = input()
            my_zoo.search_animal_by_name_json(i, my_json)
        if i == '2':
            print("Enter the animal's name:")
            i = input()
            print(my_zoo.search_animal_by_name_csv(i, my_csv))
        if i == '3':
            pass
    elif n == '5':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print("Enter the animal's ID")
            i = input()
            my_zoo.search_animal_by_id_json(i, my_json)
        if i == '2':
            print("Enter the animal's ID")
            i = input()
            my_zoo.search_animal_by_id_csv(i, my_csv)
        if i == '3':
            pass
    elif n == '6':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            print("enter the animal type:")
            i = input()
            if i == "Lion" or i == "Snake" or i == "Elephant":
                my_zoo.count_by_type_json(i, my_json)
            else:
                print("this animal type isn't exist in zoo")
        if i == '2':
            print("enter the animal type:")
            i = input()
            if i == "Lion" or i == "Snake" or i == "Elephant":
                my_zoo.count_by_type_csv(i, my_csv)
            else:
                print("this animal type isn't exist in zoo")
        if i == '3':
            pass
    elif n == '7':
        print ('Select your storage:\n1- json\n2- csv\n3- SQL db')
        i = input()
        if i == '1':
            my_zoo.count_all_animals_json(my_json)
        if i == '2':
            my_zoo.count_all_animals_csv(my_csv)
        if i == '3':
            pass

    else:
        print('please just type a number from 1 to 7')

while True:
    show_menu()
    print("\nDo you want to continue? (y/n)")
    answer = input().lower()
    if answer != 'y':
        print("Byebye!")
        break