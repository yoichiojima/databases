# databases
Snippets to handle different kinds of databases from python.

## PostgreSQL
cheatsheet: https://postgrescheatsheet.com/#/tables
### maneging roles
create firts custom roles for specific manipulations like readonly and readwrite. then inherit to other users for application use.

```postgres
CREATE DATABASE db;

<!-- create readonly role -->
CREATE ROLE readonly;
REVOKE ALL PRIVILEGES ON DATABASE db FROM readonly;
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;


<!-- create readwrite role -->
CREATE ROLE readwrite;
REVOKE ALL PRIVILEGES ON DATABASE db FROM readwrite;
GRANT CREATE ON DATABASE db FROM readwrite;
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO readwrite;

<!-- create readonly user -->
CREATE USER user_readonly WITH PASSWORD 'password';
GRANT readonly TO user_readonly;

<!-- create writeonly user -->
CREATE USER user_readwrite WITH PASSWORD 'password';
GRANT readwrite TO user_readwrite;
```

### using postgresql from python
```python
## how to create connection engine with sqlalchemy
from sqlalchemy import create_engine

user     = "user"
password = "password"
host     = "localhost"
port     = 5432
db       = "database"

engine = create_engine(
    f"postgresql://{user}:{password}@{host}:{port}/{db}",
)
```