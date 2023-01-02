import pandas as pd
import seaborn as sns
import sqlalchemy


class PostgresClient:
    def __init__(
        self,
        user: str,
        password: str,
        database: str,
        host: str = "localhost",
        port: int = 5432,
    ):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port
        self.sample_data = self.load_sample_data()

    def __repr__(self):
        return (
            f"Postgres(user={self.user}, password={self.password}, "
            f"host={self.host}, port={self.port}, database={self.database})"
        )

    def create_engine(self) -> sqlalchemy.engine:
        return sqlalchemy.create_engine(
            f"postgresql://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )

    def read_sql(self, query: str) -> pd.DataFrame:
        return pd.read_sql(query, con=self.create_engine())

    def execute_sql(self, sql: str):
        with self.create_engine().connect() as connection:
            connection.execute(sql)

    def insert(self, table: str, columns: list, values: list):
        columns = [f'"{i}"' for i in columns]
        columns = ", ".join(columns)
        values = ", ".join(values)
        sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.execute_sql(sql)

    def delete(self, table: str, condition: str):
        sql = f"DELETE FROM {table} WHERE {condition}"
        self.execute_sql(sql)

    def list_tables(self) -> pd.DataFrame:
        sql = """
            SELECT *
            FROM pg_catalog.pg_tables
            WHERE schemaname != 'pg_catalog' AND
                schemaname != 'information_schema';
        """
        return self.read_sql(sql)
