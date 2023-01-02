import pandas as pd

from postgres import PostgresClient

psql = PostgresClient(user="readwrite_user", password="postgres", database="p")


print(psql.read_sql("SELECT * FROM url"))

psql.insert("url", ["date", "url"], ["'2020-01-01'", "'https://www.google.com'"])

psql.delete("url", "url = 'https://www.google.com'")
