from storage.csv_storage import CsvStorage
from animals.Lion import Lion
import os

def test_csv_storage_save_and_load():
    lion = Lion("L002", "leo", 3, 170, 28, 55, 45, "alpha", 85)
    storage = CsvStorage()
    storage.save(lion)

    result = storage.load()
    assert any("leo" in str(item) for item in result)


    # if os.path.exists("animals.csv"):
    #     os.remove("animals.csv")
