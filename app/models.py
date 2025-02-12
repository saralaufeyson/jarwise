import json
import os

DATA_FILE = "finance_tracker.json"

# Function to load data from JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"users": [], "jars": [], "transactions": []}

# Function to save data to JSON
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# User Model (JSON-based)
class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def save(self):
        data = load_data()
        data["users"].append(self.__dict__)
        save_data(data)

    @staticmethod
    def get_by_username(username):
        data = load_data()
        for user in data["users"]:
            if user["username"] == username:
                return User(**user)
        return None

# Jar Model (JSON-based)
class Jar:
    def __init__(self, name, allocated, spent, owner):
        self.name = name
        self.allocated = allocated
        self.spent = spent
        self.owner = owner  # Username of owner

    def save(self):
        data = load_data()
        data["jars"].append(self.__dict__)
        save_data(data)

    @staticmethod
    def get_by_owner(username):
        data = load_data()
        return [Jar(**jar) for jar in data["jars"] if jar["owner"] == username]

# Transaction Model (JSON-based)
class Transaction:
    def __init__(self, amount, description, type, jar_name, owner):
        self.amount = amount
        self.description = description
        self.type = type  # "income" or "expense"
        self.jar_name = jar_name
        self.owner = owner  # Username of owner

    def save(self):
        data = load_data()
        data["transactions"].append(self.__dict__)
        save_data(data)

    @staticmethod
    def get_by_owner(username):
        data = load_data()
        return [Transaction(**t) for t in data["transactions"] if t["owner"] == username]
