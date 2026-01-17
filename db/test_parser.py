from .parser import Parser

parser = Parser()

cmd1= "INSERT INTO users (id, name) VALUES (1, 'Alice')"
cmd2 = "SELECT * FROM users WHERE id = 1"
cmd3 = "SELECT * FROM users"

print(parser.parse(cmd1))
print(parser.parse(cmd2))
print(parser.parse(cmd3))