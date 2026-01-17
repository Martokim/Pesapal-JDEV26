class Column:
    def __init__(self, name,col_type, primary=False, unique=False):
        self.name = name 
        self.col_type = col_type
        self.primary = primary
        self.unique = unique    
 
class Table: 
    def __init__(self, name, columns):
        self.name = name 
        self.columns = columns 
        self.rows = []

        self.primary_key = None
        self.unique_columns = set()

        for col in columns:
            if col.primary:
                self.primary_key = col.name
                self.unique_columns.add(col.name)
            if col.unique:
                self.unique_columns.add(col.name)

    def insert(self,row):
        #validate columns
        for col in self.columns:
            if col.name not in row:
                raise ValueError(f"Missing column: {col.name}")
        
        #validate unique constraints
        for col_name in self.unique_columns:
            for existing in self.rows:
                if existing[col_name] == row[col_name]:
                    raise ValueError(f"Duplicate value for UNIQUE column: {col_name}")
        self.rows.append (row)
                

    def select_all(self):
        return self.rows

    def select_where(self, column, value):
        return [row for row in self.rows if row[column] == value]
