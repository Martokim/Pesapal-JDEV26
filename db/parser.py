import re

class Parser:
    def __init__(self):
        # Patterns for basic SQL
        self.insert_pattern = r"INSERT INTO (\w+)\s*\((.*?)\)\s*VALUES\s*\((.*?)\)"
        self.select_pattern = r"SELECT \* FROM (\w+)(?:\s+WHERE\s+(\w+)\s*=\s*(.*))?"

    def _parse_value(self, value):
        value = value.strip().strip("'").strip('"')
        if value.isdigit():
            return int(value)
        return value

    def parse(self, command):
        command = command.strip()

        # 1. Handle INSERT
        insert_match = re.fullmatch(self.insert_pattern, command, re.IGNORECASE)
        if insert_match:
            table_name, cols_str, vals_str = insert_match.groups()
            columns = [c.strip() for c in cols_str.split(",")]
            values = [self._parse_value(v) for v in vals_str.split(",")]

            return {
                "action": "INSERT",
                "table": table_name,
                "data": dict(zip(columns, values))
            }

        # 2. Handle SELECT
        select_match = re.fullmatch(self.select_pattern, command, re.IGNORECASE)
        if select_match:
            table_name, col_name, value = select_match.groups()

            condition = None
            if col_name:
                condition = {
                    "column": col_name,
                    "value": self._parse_value(value)
                }

            return {
                "action": "SELECT",
                "table": table_name,
                "condition": condition
            }

        raise Exception("Syntax Error: Command not recognized.")
