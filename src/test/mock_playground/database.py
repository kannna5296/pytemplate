import datetime


class DatabaseConnection:
    def __init__(self, url:str, port:int):
        self.url = url
        self.port = port

# テスト対象を想定
def get_annimals(database: DatabaseConnection, species: str):
    pass
