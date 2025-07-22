import os
import json
from .abstract_storage import AbstractStorage
from animals.Lion import Lion
from animals.Elephant import Elephant
from animals.Snake import Snake

class JsonStorage(AbstractStorage):
    def save(self, l):
        if l.__class__.__name__ == "Lion":
            d = Lion.make_dict(l)
        elif l.__class__.__name__ == "Snake":
            d = Snake.make_dict(l)
        elif l.__class__.__name__ == "Elephant":
            d = Elephant.make_dict(l)
        else:
            raise ValueError("Invalid answer")
        
        file_path = "animals.json"
        animals = []
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                try:
                    animals = json.load(f)
                except:
                    animals = []
        
        animals.append(d)

        with open("animals.json", "w") as f:
            json.dump(animals, f)

    def load(self):
        with open("animals.json", "r") as f:
            data = json.load(f)
            for animal in data:
                if animal["type"] == "Lion":
                    ins = Lion.from_dict(animal)
                elif animal["type"] == "Snake":
                    ins = Snake.from_dict(animal)
                elif animal["type"] == "Elephant":
                    ins = Elephant.from_dict(animal)
                else:
                    continue 
                print(ins)

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
    
    def search_by_id(self, unique_id):
        finded_animals = []
        if not os.path.exists("animals.json"):
            return None

        with open("animals.json", "r") as f:
            try:
                animals = json.load(f)
            except:
                return finded_animals

        for animal in animals:
            if animal["unique_id"] == unique_id:
                finded_animals.append(animal)
                
        return print(finded_animals)

    def search_by_name(self, name):
        finded_animals = []
        if not os.path.exists("animals.json"):
            return  None

        with open("animals.json", "r") as f:
            try:
                animals = json.load(f)
            except:
                return None

        for animal in animals:
            if animal["name"] == name:
                finded_animals.append(animal)

        return print(finded_animals)

    def count_by_type(self, animal_type):
        count = 0
        if not os.path.exists("animals.json"):
            return count

        with open("animals.json", "r") as f:
            try:
                animals = json.load(f)
            except:
                return count

        for animal in animals:
            if animal["type"] == animal_type:
                count += 1

        return print(count)

    def count_all_animals(self):
        if not os.path.exists("animals.json"):
            return None

        with open("animals.json", "r") as f:
            try:
                animals = json.load(f)
                return len(animals)
            except:
                return 0
