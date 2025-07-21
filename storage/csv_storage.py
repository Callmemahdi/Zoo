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
        if not os.path.exists("animals.csv"):
            return

        with open("animals.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["type"] == "Lion":
                    ins = Lion.from_dict(row)
                elif row["type"] == "Snake":
                    ins = Snake.from_dict(row)
                elif row["type"] == "Elephant":
                    ins = Elephant.from_dict(row)
                else:
                    continue
                print(ins)
    
    def delete(self, unique_id):
        pass