from db.engine import Column, Table

users = Table(
    "users",
    [
        Column("id", "INT", primary=True),
        Column("email", "STRING", unique=True),
        Column("name", "STRING")
    ]
)

users.insert({"id": 1, "email": "a@b.com", "name": "Martin"})
users.insert({"id": 2, "email": "b@b.com", "name": "Kimani"})

print(users.select_where("id", 1))
print(users.select_where("email", "b@b.com"))
