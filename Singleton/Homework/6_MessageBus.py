"""
Класс MessageBus — это глобальная система обмена сообщениями внутри программы.

Назначение класса:
- хранить сообщения в общей очереди;
- давать возможность разным частям программы публиковать сообщения;
- позволять читать последние сообщения из одного централизованного места.

Важно: весь проект должен использовать только ОДИН экземпляр MessageBus,
поэтому необходимо реализовать паттерн Singleton.
"""

class MessageBus:
    _instance = None

    def __new__(cls):
        # TODO: реализовать Singleton — возвращать один и тот же объект MessageBus
        pass

    def __init__(self):
        # Очередь сообщений (список)
        self._messages = []

    def publish(self, message):
        # TODO: добавить новое сообщение в очередь
        pass

    def read_last(self):
        # TODO: вернуть последнее сообщение или None, если сообщений нет
        pass

    def clear(self):
        # TODO: очистить очередь сообщений
        pass


# --- Тестовый код ---
bus1 = MessageBus()
bus2 = MessageBus()

print("Same instance?", bus1 is bus2)  # должно быть True

bus1.publish("System started")
bus1.publish("User logged in")

print(bus2.read_last())  # должно вывести "User logged in"

bus2.clear()

print(bus1.read_last())  # должно вывести None
