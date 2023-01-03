from redis import Redis
import json

class RedisClient:
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.host = host
        self.port = port
        self.db = db
        self.instance = Redis(host=host, port=port, db=db)

    def __repr__(self):
        return f"RedisClient(host={self.host}, port={self.port}, db={self.db})"
        
    def set(self, key: str, values: dict | list | str):
        self.instance.set(key, json.dumps(values))

    def get(self, key: str) -> dict | list | str:
        return json.loads(self.instance.get(key))