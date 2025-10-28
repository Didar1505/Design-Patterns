class ConfigurationManager:
    _instance = None
    _initialized = False # 1. Добавляем флаг "уже инициализирован?"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # 2. Проверяем, был ли этот ОБЪЕКТ уже инициализирован
        if self._initialized:
            # Если да, ничего не делаем
            print("Инициализация (__init__) уже была, пропускаю.")
            return

        # 3. Если нет, то инициализируем
        print("Запускаю ПЕРВИЧНУЮ инициализацию (__init__)")
        self._settings = {"database_url": "sql://...", "api_key": "12345"}
        
        # 4. Ставим флаг, что мы закончили
        self._initialized = True 

    # ...остальные методы...
    def get_setting(self, key: str):
        return self._settings.get(key)


# --- Проверяем ---
print("Попытка 1:")
c1 = ConfigurationManager() # __init__ выполнится
print(f"Ключ: {c1.get_setting('api_key')}")

# Меняем значение
c1._settings["api_key"] = "НОВЫЙ_КЛЮЧ"
print(f"Новый ключ: {c1.get_setting('api_key')}")


print("\nПопытка 2:")
c2 = ConfigurationManager() # __init__ НЕ выполнится (благодаря флагу)
print(f"Ключ из c2: {c2.get_setting('api_key')}") # Увидим "НОВЫЙ_КЛЮЧ"