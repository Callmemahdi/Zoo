import os
import csv
from .abstract_storage import AbstractStorage
from animals.Lion import Lion
from animals.Elephant import Elephant
from animals.Snake import Snake



class CsvStorage(AbstractStorage):
    def save(self, animal):
        if animal.__class__.__name__ == "Lion":
            row = Lion.make_dict(animal)
            filename = "lions.csv"
        elif animal.__class__.__name__ == "Snake":
            row = Snake.make_dict(animal)
            filename = "snakes.csv"
        elif animal.__class__.__name__ == "Elephant":
            row = Elephant.make_dict(animal)
            filename = "elephants.csv"
        else:
            raise ValueError("Invalid animal type")

        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as f:
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
        if not os.path.exists("animals.csv"):
            return

        with open("animals.csv", "r") as f:
            reader = csv.DictReader(f)
            animals = []
            for row in reader :
                if row["unique_id"] != unique_id:
                    animals.append(row)
        
        with open("animals.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=animals[0].keys())
            writer.writeheader()
            writer.writerows(animals)