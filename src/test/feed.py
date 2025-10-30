from datetime import datetime, timedelta


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


def get_food_period(database: DatabaseConnection, species: str) -> timedelta:
    return timedelta(days=1)


def feed_animal(database: DatabaseConnection, species: str, now: datetime):
    pass


def do_rounds(
    database,
    species,
    *,
    # キーワード引数のみ。
    # OK （do_rounds(database, species, now_func=datetime.now...)
    # NG （do_rounds(database, species, datetime.now...)）
    now_func=datetime.now,
    food_func=get_food_period,
    animals_func=get_animals,
    feed_func=feed_animal,
):
    now = now_func()
    feeding_timedelta = food_func(database, species)
    animals = animals_func(database, species)
    fed = 0

    for name, last_mealtime in animals.items():
        print(f"name: {name}, now-last_mealtime: {now - last_mealtime}, feeding_timedelta: {feeding_timedelta}")
        if (now - last_mealtime) > feeding_timedelta:
            feed_func(database, name, now)
            fed += 1

    return fed
