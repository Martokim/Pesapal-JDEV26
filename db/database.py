from db.engine import Table, Column

class MiniDatabase:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, columns):
        self.tables[name] = Table(name, columns)

    def get_table(self, name):
        if name not in self.tables:
            raise Exception(f"Table '{name}' does not exist")
        return self.tables[name]
