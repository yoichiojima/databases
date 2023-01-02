import pandas as pd
import seaborn as sns

from postgres import PostgresClient

psql = PostgresClient(user="readwrite_user", password="postgres", database="p")


def fetch_len():
    initial_data = psql.read_sql("select * from diamonds")
    return len(initial_data)


def test_to_sql():
    assert fetch_len() == 0
    df = sns.load_dataset("diamonds")
    psql.to_sql(df, "diamonds", if_exists="replace")
    assert fetch_len() == 53940


def test_delete():
    assert fetch_len() == 53940
    psql.delete("diamonds", "")
    assert fetch_len() == 0
