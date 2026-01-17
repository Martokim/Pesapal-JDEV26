class Index:
    def __init__(self):
        self.data = {}

    def add(self, key, row):
        self.data[key] = row

    def get(self, key):
        return self.data.get(key)

    def exists(self, key):
        return key in self.data
