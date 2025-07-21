#temp
# from animals.Elephant import Elephant
animal_list = []

class Zoo():
    def add_animal(self, animal):
        animal_list.append(animal)


    def add_animal_json(self, l, my_json):
        my_json.save(l)

    def add_animal_csv(self,l,my_csv):
        my_csv.save(l)
        
    def remove_animal(self, unique_id):
        for animal in animal_list:
            if animal.unique_id == unique_id:
                animal_list.remove(animal)

    def show_animals(self):
        for animal in animal_list:
            print(animal)

    def show_animals_json(self, my_json):
        my_json.load()
    
    def show_animals_csv(self, my_csv):
        my_csv.load()

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

    def count_all_animals(self):
        print(len(animal_list))
# e = Elephant('E001', 'Horton', 11, 3500, 450, 250, 'Asian', 'jungle', 43,)
# print (e.unique_id)
    