from db.parser import Parser
from db.executor import Executor
from db.database import MiniDatabase
from db.engine import Column

def start_repl():
    print("MiniRDBMS interactive shell")
    print("Type 'exit' or 'quit' to leave")

    parser = Parser()
    db = MiniDatabase()
    executor = Executor(db)

    # Temporary demo table (we'll improve later)
    db.create_table(
        "users",
        [
            Column("id", "INT", primary=True),
            Column("email", "STRING", unique=True),
            Column("name", "STRING")
        ]
    )

    while True:
        try:
            command = input("db> ").strip() 
            if not command:
                continue            
            if command.lower() in ("exit", "quit"):
                break

            if command.lower() == "help":
                print("Supported commands:")
                print(" INSERT INTO table (columns) VALUES (values)")
                print(" SELECT * FROM table (cols) VALUES (values ) ")
                print(" SELECT * FROM table")
                print(" SELECT * FROM table WHERE column = value")
                continue
            
            parsed = parser.parse(command)
            result = executor.execute(parsed)
            print(result)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    start_repl()
