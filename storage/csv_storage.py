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
        all_files = {
            "Lion": "lions.csv",
            "Snake": "snakes.csv",
            "Elephant": "elephants.csv"
        }

        for animal_type, filename in all_files.items():
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    lines = f.readlines()
                    if lines:
                        print(animal_type.upper())
                        for line in lines:
                            print(line.strip())
                        print()


    def delete(self, unique_id):
        files = ["lions.csv", "snakes.csv", "elephants.csv"]
        for file in files:
            if not os.path.exists(file):
                continue

            with open(file, "r") as f:
                reader = csv.DictReader(f)
                animals = list(reader)

            new_animals = []
            for row in animals:
                if row["unique_id"].strip() != unique_id.strip():
                    new_animals.append(row)

            if len(new_animals) != len(animals):
                with open(file, "w", newline='') as f:
                    if new_animals:
                        writer = csv.DictWriter(f, fieldnames=new_animals[0].keys())
                        writer.writeheader()
                        writer.writerows(new_animals)
                print("Animal deleted")
                return

        print("Animal not found")



    def search_by_id(self, unique_id):
        files = ["lions.csv", "snakes.csv", "elephants.csv"]
        for file in files:
            if not os.path.exists(file):
                continue
            with open(file, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["unique_id"].strip() == unique_id.strip():
                        print(row)
                        return
        print("Not found")

    def search_by_name(self, name):
        files = ["lions.csv", "snakes.csv", "elephants.csv"]
        

        for file in files:
            if not os.path.exists(file):
                continue
            with open(file, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["name"] == name:
                        print (row)
                        return
                        #return finded_animals
        
    def count_by_type(self, type):
        files = ["lions.csv", "snakes.csv", "elephants.csv"]
        count = 0

        for file in files:
            if os.path.exists(file):
                with open(file, "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["type"] == type:
                            count +=1
            else:
                continue
        return print(count)

    def count_all_animals(self):
        files = ["lions.csv", "snakes.csv", "elephants.csv"]
        count = 0

        for file in files:
            if os.path.exists(file):
                with open(file, "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                            count +=1
            else:
                continue
        return print(count)