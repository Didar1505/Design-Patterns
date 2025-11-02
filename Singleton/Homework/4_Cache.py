class Cache:
    _instance = None

    def __new__(cls):
        # TODO: реализовать поведение Singleton — всегда возвращать один и тот же объект
        pass

    def __init__(self):
        # Внутреннее хранилище (словарь)
        self._store = {}

    def set(self, key, value):
        # TODO: сохранить значение под указанным ключом
        pass

    def get(self, key, default=None):
        # TODO: вернуть значение по ключу, если оно существует, иначе вернуть default
        pass

    def delete(self, key):
        # TODO: удалить элемент по ключу, если он существует
        pass

    def clear(self):
        # TODO: полностью очистить кэш
        pass


# --- Тестовый код ---
cache1 = Cache()
cache2 = Cache()

print("Same instance?", cache1 is cache2)  # должно быть True

cache1.set("user", "Alice")
print(cache2.get("user"))  # должно вывести "Alice"
