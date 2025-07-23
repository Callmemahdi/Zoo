from storage.json_storage import JsonStorage
from animals.Lion import Lion
import os

def test_json_storage_save_and_load():
    lion = Lion("L001", "leo", 4, 180, 30, 60, 50, "beta", 90)
    storage = JsonStorage()
    storage.save(lion)

    result = storage.load()
    assert any("leo" in str(item) for item in result)
