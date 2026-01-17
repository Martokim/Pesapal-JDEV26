from db.index import Index 
class Column:
    def __init__(self, name,col_type, primary=False, unique=False):
        self.name = name 
        self.col_type = col_type
        self.primary = primary
        self.unique = unique    
 
class Table: 
    def __init__(self, name, columns):
        self.indexes = {}
        self.name = name 
        self.columns = columns 
        self.rows = []

        self.primary_key = None
        self.unique_columns = set()

        for col in columns:
            if col.primary or col.unique:
                self.indexes[col.name] = Index()
            if col.unique:
                self.unique_columns.add(col.name)

    def insert(self,row):
        #validate columns
        for col in self.columns:
            if col.name not in row:
                raise ValueError(f"Missing column: {col.name}")
        
        #validate unique constraints
        for col_name in self.unique_columns:
            index = self.indexes[col_name]
            if index.exists(row[col_name]):
                    raise ValueError(f"Duplicate value for UNIQUE column: {col_name}")
        self.rows.append (row)
    
        #update indexes
        for col_name, index in self.indexes.items():
            index.add(row[col_name], row)   
                

    def select_all(self):
        return self.rows

    def select_where(self, column, value):
        if column in self.indexes:
            result = self.indexes[column].get(value)
            return [result] if result else []
        return [row for row in self.rows if row[column] == value]
