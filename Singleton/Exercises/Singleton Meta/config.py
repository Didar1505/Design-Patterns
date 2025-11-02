from singleton_meta import SingletonMeta

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.theme = "Light"
        self.language = "EN"

    def set_theme(self, theme):
        self.theme = theme

    def set_language(self, language):
        self.language = language
