import os
import json
from .abstract_storage import AbstractStorage
from animals.Lion import Lion
from animals.Elephant import Elephant
from animals.Snake import Snake
from animals.animal_factory import AnimalFactory

class JsonStorage(AbstractStorage):
    def save(self, animal_data):
        try:
            file_path = "animals.json"
            animals = []
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    try:
                        animals = json.load(f)
                    except:
                        animals = []            
            animals.append(animal_data)

            with open("animals.json", "w") as f:
                json.dump(animals, f)
        except:
            raise ValueError

    def load(self):
        with open("animals.json", "r") as f:
            data = json.load(f)            
            for animal in data:
                print(json.dumps(animal, indent = 2))
            return data
                # if animal["type"] == "Lion":
                #     ins = Lion.from_dict(animal)
                #     show_animals.append(ins)
                # elif animal["type"] == "Snake":
                #     ins = Snake.from_dict(animal)
                #     show_animals.append(ins)
                # elif animal["type"] == "Elephant":
                #     ins = Elephant.from_dict(animal)
                #     show_animals.append(ins)
                # else:
                #     continue 

    def delete(self, unique_id):
        animals = []

        if os.path.exists("animals.json"):
            with open("animals.json", "r") as f:
                try:
                    animals = json.load(f)
                except:
                    animals = []

        new_animals = []
        for a in animals:
            if a["unique_id"] != unique_id:
                new_animals.append(a)
        if len(new_animals) == len(animals):
            return False
        
        with open("animals.json", "w") as f:
            json.dump(new_animals, f)

        return True
    
    def search_by_id(self, id):
        if not os.path.exists("animals.json"):
            return None

        with open("animals.json", "r") as f:
            try:
                animals = json.load(f)
            except:
                return None

        for animal in animals:
            if animal["unique_id"] == id:
                print(animal)
                return animal                
        return None

    def search_by_name(self, name):
        if not os.path.exists("animals.json"):
            return  None

        with open("animals.json", "r") as f:
            try:
                animals = json.load(f)
            except:
                return None
            
        for animal in animals:
            if animal["name"] == name:
                print(animal)
                return(animal)

    def count_by_type(self, group):
        count = 0
        if not os.path.exists("animals.json"):
            return count

        with open("animals.json", "r") as f:
            try:
                animals = json.load(f)
            except:
                return count

        for animal in animals:
            if animal["type"] == group:
                count += 1
        print(count)
        return count
    
    def count_all_animals(self):
        if not os.path.exists("animals.json"):
            return None

        with open("animals.json", "r") as f:
            try:
                animals = json.load(f)
                return len(animals)
            except:
                return 0

