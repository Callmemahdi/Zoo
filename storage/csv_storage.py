import os
import csv
from .abstract_storage import AbstractStorage
from animals.Lion import Lion
from animals.Elephant import Elephant
from animals.Snake import Snake
import json


class CsvStorage(AbstractStorage):
    def save(self, animal):

        """
        Saves an animal to a CSV file
        """
    
        # if animal.__class__.__name__ == "Lion":
        #     row = Lion.make_dict(animal)
        #     filename = "lions.csv"
        # elif animal.__class__.__name__ == "Snake":
        #     row = Snake.make_dict(animal)
        #     filename = "snakes.csv"
        # elif animal.__class__.__name__ == "Elephant":
        #     row = Elephant.make_dict(animal)
        #     filename = "elephants.csv"
        # else:
        #     raise ValueError("Invalid animal type")
        file_path = f"{animal['type']}.csv"
        file_exists = os.path.exists(file_path)
        # file_exists = os.path.exists(filename)

        with open(file_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=animal.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(animal)

    def load(self):
        """
        Prints all animals from the CSV files to the console
        """
        all_files = {
            "Lion": "Lion.csv",
            "Snake": "Snake.csv",
            "Elephant": "Elephant.csv"
        }

        for animal_type, filename in all_files.items():
            if os.path.exists(filename):
                print(f"\n{animal_type.upper()}:")
                with open(filename, "r", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        print (row)
                        # print(json.dumps(row, indent=2))
                    # if lines:
                    #     print(animal_type.upper())
                    #     show_lines = []
                    #     for line in lines:
                    #         show_lines.append(line.strip())
                    #         print(line.strip())
                    #     print()
                    # return show_lines

    def delete(self, unique_id):

        """
        Deletes an animal from the CSV files based on its unique ID.
        """
        files = ["Lion.csv", "Snake.csv", "Elephant.csv"]
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
                        print(writer)
                #print("Animal deleted")
                return True
        return False

    def search_by_id(self, unique_id):

        """
        Searches through the CSV files to find and print an animal with the specified unique ID.
        """

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
        """
        Searches through the CSV files to find and print animals with the specified name.
        """
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
        """
        Counts and prints the number of animals of the specified type in the CSV files.
        """
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
        """
        Counts and prints the total number of animals in the CSV files.
        """
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