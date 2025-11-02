from game_settings import GameSettings

class Player:
    def __init__(self, name):
        self.name = name
        # Every player shares the same GameSettings object
        self.settings = GameSettings()

    def show_settings(self):
        print(f"{self.name}'s view:")
        print(f"Volume: {self.settings.volume}")
        print(f"Difficulty: {self.settings.difficulty}")
        print(f"Full Screen: {self.settings.full_screen}")
