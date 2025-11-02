import json 
import os

class ConfigManager:
    _instance = None
    _config = None

    def __new__(cls, confgi_path=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)    
            if confgi_path:
                cls._instance.load_config(confgi_path)
        return cls._instance
    
    def load_config(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError("File not found in given path", path)
        
        with open(path, mode='r') as file:
            self._config = json.load(file)
        
    def get(self, key, default=None):
        return self._config.get(key, default)
    
    def add_admin(self, username, password):
        data = {
            'username': username, 
            'password': password
        }
        self._config["admins"].append(data)
    
    def __str__(self):
        return json.dumps(self._config, indent=2)