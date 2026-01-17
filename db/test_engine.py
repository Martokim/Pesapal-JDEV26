from engine import Column , Table 

cols = [
    Column("id", "int", primary=True),
    Column("email", "str", unique=True),
    Column("name", "str")
]

users = Table("users", cols) 
users.insert({"id":1, "email":"a@b.com", "name":"Martin"})
users.insert({"id": 2 , "email": "b@b.com", "name":"kimani"})

print(users.select_all())
print(users.select_where("id",1))