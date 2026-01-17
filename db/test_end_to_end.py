from db.parser import Parser
from db.database import MiniDatabase
from .executor import Executor
from .engine import Column

db = MiniDatabase()
db.create_table(
    "users",
    [
        Column("id", "INT", primary=True),
        Column("name", "STRING")
    ]
)

parser = Parser()
executor = Executor(db)

cmds = [
    "INSERT INTO users (id, name) VALUES (1, 'Martin')",
    "INSERT INTO users (id, name) VALUES (2, 'Kimani')",
    "SELECT * FROM users",
    "SELECT * FROM users WHERE id = 1"
]

for c in cmds:
    parsed = parser.parse(c)
    result = executor.execute(parsed)
    print(result)
