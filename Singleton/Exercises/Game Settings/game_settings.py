class GameSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return

        # Default settings
        self.volume = 50          # 0–100
        self.difficulty = "Medium"
        self.full_screen = False

        self._initialized = True

    def set_volume(self, vol):
        self.volume = vol

    def toggle_full_screen(self):
        self.full_screen = not self.full_screen

    def set_difficulty(self, level):
        self.difficulty = level
