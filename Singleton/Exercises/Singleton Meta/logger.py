from singleton_meta import SingletonMeta

class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)

    def show_logs(self):
        print(self.logs)
