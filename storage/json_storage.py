import json
from .abstract_storage import AbstractStorage
from animals.Elephant import Elephant
from animals.Lion import Lion
from animals.Snake import Snake


class JsonStorage(AbstractStorage):
    def save(self, l):
        if l.__class__.__name__ == "Lion":
            j = Lion.make_dict(l)
            with open("animals.json", "a") as f:
                json.dump(j, f)
        elif l.__class__.__name__ == "Snake" :
            j = Snake.make_dict(l)
            with open("animals.json", "a") as f:
                json.dump(j, f)
        elif l.__class__.__name__ == "Elephant" :
            j = Elephant.make_dict(l)
            with open("animals.json", "a") as f:
                json.dump(j, f) 
    def load(self):
        pass
    def delete(self, unique_id):
        pass
    