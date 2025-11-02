import json
import os

class Database:
    _instance = None

    def __new__(cls):
        pass

    def __init__(self, db_file="db.json"):
        # if hasattr(self, "_initialized") and self._initialized:
        #     return

        self.db_file = db_file
        self.data = {"users": {}}

        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = {"users": {}}
        else:
            self.save()

        self._initialized = True

    def save(self):
        with open(self.db_file, mode='w') as file:
            json.dump(self.data, file, indent=2)

    def add_user(self, username, role):
        self.data["users"][username] = {"role": role}
        self.save()

    def get_user(self, username):
        if username in self.data['users']:
            return self.data['users'][username]['role']
        else:
            return "Guest"
    
    def list_users(self):
        return self.data['users']
