from pymongo import MongoClient


class MongoDB:
    def __init__(self, host: str = "localhost", port: int = 27017):
        self.client = MongoClient(host, port)
    
    def __repr__(self):
        return f"MongoDB({self.client.host}, {self.client.port})"