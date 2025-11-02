class Settings:
    _instance = None

    def __new__(cls):
        # TODO: реализовать поведение Singleton — вернуть один и тот же объект
        pass

    def __init__(self):
        # Начальные настройки приложения
        self._config = {
            "theme": "light",
            "language": "EN",
            "volume": 50
        }

    def set(self, key, value):
        # TODO: изменить значение настройки по ключу
        pass

    def get(self, key, default=None):
        # TODO: вернуть значение настройки, если она существует
        pass

    def show_all(self):
        # TODO: вывести все настройки (например, распечатать self._config)
        pass


# --- Тестовый код ---
s1 = Settings()
s2 = Settings()

print("Same instance?", s1 is s2)  # должно быть True

s1.set("theme", "dark")
s1.set("volume", 80)

print(s2.get("theme"))   # должно вывести "dark"
print(s2.get("volume"))  # должно вывести 80

s2.show_all()  # должно отобразить текущие настройки
