import os
import csv
from .abstract_storage import AbstractStorage
from animals.Lion import Lion
from animals.Elephant import Elephant
from animals.Snake import Snake



class CsvStorage(AbstractStorage):
    def save(self, l):
        if l.__class__.__name__ == "Lion":
            row = Lion.make_dict(l)
        elif l.__class__.__name__ == "Snake":
            row = Snake.make_dict(l)
        elif l.__class__.__name__ == "Elephant":
            row = Elephant.make_dict(l)
        else:
            raise ValueError("Invalid animal type")

        file_exists = os.path.exists("animals.csv")

        with open("animals.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)


    def load(self):
        pass
    
    def delete(self, unique_id):
        pass