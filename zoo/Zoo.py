#temp
# from animals.Elephant import Elephant
#animal_list = []

class Zoo():
    

    def add_animal_json(self, l, my_json):
        my_json.save(l)

    def add_animal_csv(self,l,my_csv):
        my_csv.save(l)

    def show_animals_json(self, my_json):
        my_json.load()

    def show_animals_csv(self, my_csv):
        my_csv.load()

    def remove_animal_json(self, unique_id, my_json):
        my_json.delete(unique_id)
    
    def remove_animal_csv(self, unique_id, my_csv):
        my_csv.delete(unique_id)

    def search_animal_by_name_json(self, name, my_json):
        my_json.search_by_name(name)

    def search_animal_by_name_csv(self, name, my_csv):
        return my_csv.search_by_name(name)

    def search_animal_by_id_json(self, unique_id, my_json):
        my_json.search_by_id(unique_id)
    def search_animal_by_id_csv(self, unique_id, my_csv):
        my_csv.search_by_id(unique_id)

    def count_by_type_json(self, type, my_json):
        my_json.count_by_type(type)

    def count_by_type_csv(self, type, my_csv):
        my_csv.count_by_type(type)

    def count_all_animals_json(self, my_json):
        my_json.count_all_animals()

    def count_all_animals_csv(self, my_csv):
        my_csv.count_all_animals()
    

   
    
    





    # def add_animal(self, animal):
    #     animal_list.append(animal)

    # def remove_animal(self, unique_id):
    #     for animal in animal_list:
    #         if animal.unique_id == unique_id:
    #             animal_list.remove(animal)

    # def show_animals(self):
    #     for animal in animal_list:
    #         print(animal)

    # def serach_animal_by_name(self, name):
    #     for animal in animal_list:
    #         if animal.name == name:
    #             print(animal)

    # def search_animal_by_id(self, unique_id):
    #     for animal in animal_list:
    #         if animal.unique_id == unique_id:
    #             print(animal)

    # def count_by_type(self, type):
    #     counter = 0
    #     for animal in animal_list:
    #         if animal.__class__.__name__ == type:
    #             counter += 1
    #     print(f"The count of {type} is: {counter}")

    # def count_all_animals(self):
    #     print(len(animal_list))
# e = Elephant('E001', 'Horton', 11, 3500, 450, 250, 'Asian', 'jungle', 43,)
# print (e.unique_id)
    