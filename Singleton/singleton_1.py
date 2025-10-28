class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Создаю НОВЫЙ экземпляр ConfigurationManager")
            cls._instance = super().__new__(cls)
            cls._instance._settings = {"database_url": "sql://...", "api_key": "12345"}
        else:
            print("Возвращаю СУЩЕСТВУЮЩИЙ экземпляр")
        
        return cls._instance
    
    def get_setting(self, key):
        return self._settings.get(key)
    
print("--- Пример с Синглтоном ---")

print("Попытка 1:")
config1 = ConfigurationManager()
print(f"API Key из config1: {config1.get_setting('api_key')}")

# Второй вызов:
print("\nПопытка 2:")
config2 = ConfigurationManager()
print(f"API Key из config2: {config2.get_setting('api_key')}")

print("\nПроверка:")
if id(config1) == id(config2):
    print("config1 и config2 — это ОДИН И ТОТ ЖЕ объект в памяти. (id одинаковые)")
else:
    print("Что-то пошло не так, это разные объекты!")

config2._settings['api_key'] = '67890'
print("--")
print("Config 1:", config1._settings)
print("Config 2:", config2._settings)

