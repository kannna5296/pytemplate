from datetime import datetime, timedelta

from test.simple_test.feed import DatabaseConnection

# database情報をラップするオブジェクトを作って、カプセル化する
# ヘルパー関数を持たせる


class ZooDatabase:
    def __init__(self, database: DatabaseConnection):
        self.database = database

    def get_animals(self, species: str) -> dict[str, datetime]:
        return {
            "dog": datetime(2024, 6, 5, 11, 15),
            "cat": datetime(2024, 6, 6, 12, 30),
            "bird": datetime(2024, 6, 7, 9, 45),
        }

    def get_food_period(self, species: str) -> timedelta:
        return timedelta(days=1)

    def feed_animal(self, species: str, when: datetime):
        pass


def do_rounds(
    zoo_db: ZooDatabase,
    species: str,
    *,
    now_func=datetime.now,
):
    now = now_func()
    feeding_timedelta = zoo_db.get_food_period(species)
    animals = zoo_db.get_animals(species)
    fed = 0

    for name, last_mealtime in animals.items():
        if (now - last_mealtime) > feeding_timedelta:
            zoo_db.feed_animal(name, now)
            fed += 1

    return fed
