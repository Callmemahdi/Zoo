import os
import json
from .abstract_storage import AbstractStorage
from animals.Lion import Lion
from animals.Elephant import Elephant
from animals.Snake import Snake

class JsonStorage(AbstractStorage):
    def save(self, l):
        if l.__class__.__name__ == "Lion":
            j = Lion.make_dict(l)
        elif l.__class__.__name__ == "Snake":
            j = Snake.make_dict(l)
        elif l.__class__.__name__ == "Elephant":
            j = Elephant.make_dict(l)
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
        
        animals.append(j)

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

        with open("animals.json", "w") as f:
            json.dump(new_animals, f)

    