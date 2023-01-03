import pandas as pd
import seaborn as sns

from postgres import PostgresClient

psql = PostgresClient(user="readwrite_user", password="postgres", database="p")


def fetch_len():
    initial_data = psql.read_sql("select * from diamonds")
    return len(initial_data)


def test_to_sql():
    print(f"\ntesting to_sql\n{'=' * 50}")
    print(f"current length of tables: {fetch_len()}")
    df = sns.load_dataset("diamonds")
    psql.to_sql(df, "diamonds", if_exists="replace")
    print(f"length of tables after udpate: {fetch_len()}")


def test_delete():
    print(f"\ntest_delete\n{'=' * 50}")
    print(f"current length of tables: {fetch_len()}")
    psql.delete("diamonds", "")
    print(f"length of tables after deletion: {fetch_len()}")


def test_list_columns():
    print(f"\ntest_list_columns\n{'=' * 50}")
    df = sns.load_dataset("diamonds")
    psql.to_sql(df, "diamonds", if_exists="replace")
    print(psql.list_columns("diamonds"))
    psql.delete("diamonds")


def test_list_roles():
    print(f"\ntest_list_roles\n{'=' * 50}")
    psql = PostgresClient(user="yo", password="postgres", database="p")
    print(psql.list_roles())
