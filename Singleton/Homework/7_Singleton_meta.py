class SingletonMeta(type):
    """
    Напишите Мета-класс Singleton.
    Любой класс, использующий этот мета-класс, будет иметь только один экземпляр.
    """
    pass


class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.theme = "Light"
        self.language = "EN"

    def set_theme(self, theme):
        self.theme = theme

    def set_language(self, language):
        self.language = language


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)

    def show_logs(self):
        print(self.logs)


log1 = Logger()
log2 = Logger()
cfg1 = Config()
cfg2 = Config()

# Проверяем, что экземпляры действительно одинаковые
print("Logger instances same?", log1 is log2)
print("Config instances same?", cfg1 is cfg2)

# Тестируем общие данные логгера
log1.log("System started")
log2.log("User logged in")
log1.show_logs()  # должны отображаться оба сообщения

# Тестируем общие настройки конфигурации
cfg1.set_theme("Dark")
cfg2.set_language("FR")
print(cfg1.theme, cfg1.language)  # должно быть Dark FR
print(cfg2.theme, cfg2.language)  # должно быть Dark FR
