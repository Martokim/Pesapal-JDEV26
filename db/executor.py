class Executor:
    def __init__(self, database):
        self.db = database

    def execute(self, command):
        action = command["action"]
        table = self.db.get_table(command["table"])

        if action == "INSERT":
            table.insert(command["data"])
            return "OK"

        if action == "SELECT":
            if command["condition"] is None:
                return table.select_all()
            return table.select_where(
                command["condition"]["column"],
                command["condition"]["value"]
            )

        raise Exception("Unsupported operation")
