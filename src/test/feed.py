
from datetime import timedelta
import datetime

class DatabaseConnection:
    def __init__(self, url:str, port:int):
        self.url = url
        self.port = port

# テスト対象を想定
def get_annimals(database: DatabaseConnection, species: str):
    pass

def get_food_period(database, species) -> timedelta:
    return timedelta(days=1)

def feed_animal(database, species):
    pass

def do_rounds(database, species):
    now = datetime.now()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, species, name)
            fed += 1

    return fed
