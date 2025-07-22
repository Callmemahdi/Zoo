from zoo.Zoo import Zoo
from animals.Lion import Lion
from animals.Snake import Snake
from animals.Elephant import Elephant
from storage.csv_storage import CsvStorage

lion = Lion('l001', 'Oscar', 12, 150, 20, 80, 30, 'alpha', 110)
my_csv = CsvStorage()
from auth.permissions import Role

admin_zoo = Zoo(role=Role.ADMIN)
visitor_zoo = Zoo(role=Role.USER)

# این موفق می‌شه
admin_zoo.add_animal_csv(lion, my_csv)

# این رد می‌شه با پیام Permission denied
visitor_zoo.add_animal_csv(lion, my_csv)
