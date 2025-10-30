import datetime
from datetime import timedelta


class DatabaseConnection:
    def __init__(self, url: str, port: int):
        self.url = url
        self.port = port


# テスト対象を想定
def get_animals(database: DatabaseConnection, species: str) -> dict[str, datetime]:
    return {
        "dog": datetime(2024, 6, 5, 11, 15),
        "cat": datetime(2024, 6, 6, 12, 30),
        "bird": datetime(2024, 6, 7, 9, 45),
    }


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
