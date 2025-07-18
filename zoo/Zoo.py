#temp
# from animals.Elephant import Elephant
animal_list = []

class Zoo():
    def add_animal(self, animal):
        animal_list.append(animal)

    def remove_animal(self, unique_id):
        for animal in animal_list:
            if animal.unique_id == unique_id:
                animal_list.remove(animal)

    def show_animals(self):
        for animal in animal_list:
            print(animal)
    
    def serach_animal_by_name(self, name):
        for animal in animal_list:
            if animal.name == name:
                print(animal)

    def search_animal_by_id(self, unique_id):
        for animal in animal_list:
            if animal.unique_id == unique_id:
                print(animal)

    def count_by_type(self, type):
        counter = 0
        for animal in animal_list:
            if animal.__class__.__name__ == type:
                counter += 1
        print(f"The count of {type} is: {counter}")
# e = Elephant('E001', 'Horton', 11, 3500, 450, 250, 'Asian', 'jungle', 43,)
# print (e.unique_id)
    