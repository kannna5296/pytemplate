from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)
        print(self.data)  # defaultdict(<class 'set'>, {}) ※{}はsetの意味

    def add(self, country: str, city: str) -> None:
        self.data[country].add(city)


visits = Visits()
visits.add("England", "Batch")
visits.add("England", "London")
visits.add("USA", "Hage")
print(visits.data)


fuga = {}
print(type(fuga))
