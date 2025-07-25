from . Elephant import Elephant
from . Lion import Lion
from . Snake import Snake

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "Lion":
            return Lion(**kwargs)