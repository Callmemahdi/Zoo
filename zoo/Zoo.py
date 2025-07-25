#temp
# from animals.Elephant import Elephant
#animal_list = []
from logs.logger import logger
from auth.permissions import Role
class Zoo():
    def __init__(self, Storage, role = Role.ADMIN):
        self.role = role
        self.storage = Storage
   
    def add_animal(self, animal_data):
        if self.role != Role.ADMIN:
            print("Permission denied: only admin can add animals.")
            return
        self.storage.save(animal_data)
        logger.info(f"Added animal: {animal_data['unique_id']} ({animal_data['type']})")


    # def show_animals_json(self, my_json):
    #     my_json.load()

    # def show_animals_csv(self, my_csv):
    #     my_csv.load()
        
    def show_animals(self):
        self.storage.load()

    def remove_animal_json(self, unique_id, my_json):
        if self.role != Role.ADMIN:
            print("Permission denied: only admin can remove animals.")
            return
        my_json.delete(unique_id)
        logger.info(f"Removed animal: {unique_id}")


    # def remove_animal_csv(self, unique_id, my_csv, user):
    #     exist = my_csv.delete(unique_id)
    #     if exist:
    #         logger.info(f"Removed animal: {unique_id}")
    #     else:
    #         logger.warning(f"not exist this animall in the zoo with this ID: {unique_id}")

    def remove_animal_csv(self, unique_id, my_csv):
        if self.role != Role.ADMIN:
            print("Permission denied: only admin can remove animals.")
            return
        my_csv.delete(unique_id)
        logger.info(f"Removed animal: {unique_id}")

        
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
    