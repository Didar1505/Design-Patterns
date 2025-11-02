import hashlib
from config_manager import ConfigManager


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(str(password).encode("utf-8")).hexdigest()
        self.register()

    def register(self):
        settings = ConfigManager('config.json')
        settings.add_admin(self.username, self.password)
        print(f"Registered admin: {self.username}")