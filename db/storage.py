import json 
import os 
DATA_DIR = "DATA"

def save_table(table):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = f"{DATA_DIR}/{table.name}.json"

    data = {
        "rows": table.rows
    }

    with open (path,"w") as f:
        json.dump(data,f)

def load_table(table):
    path = f"{DATA_DIR}/{table.name}.json"

    