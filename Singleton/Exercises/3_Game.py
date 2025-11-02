class GameSettings:
    _instance = None

    def __new__(cls):
        # TODO: return the same instance every time
        pass

    def __init__(self):
        # Default settings (students can change/expand these)
        self.volume = 50            # range: 0–100
        self.difficulty = "medium"  # easy / medium / hard
        self.full_screen = False

    def set_volume(self, value):
        # TODO: validate and apply volume
        pass

    def set_difficulty(self, level):
        # TODO: ensure level is one of: easy, medium, hard
        pass

    def toggle_full_screen(self):
        # TODO: switch full_screen between True/False
        pass


# --- Test Code ---
s1 = GameSettings()
s2 = GameSettings()

print("Same instance?", s1 is s2)   # should be True

s1.set_volume(80)
print(s2.volume)   # should be 80 once implemented
