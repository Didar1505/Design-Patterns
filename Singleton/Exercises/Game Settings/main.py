from player import Player

# Create two players
p1 = Player("Alice")
p2 = Player("Bob")

# Show default settings
p1.show_settings()
p2.show_settings()

# Change settings via p1
p1.settings.set_volume(80)
p1.settings.set_difficulty("Hard")
p1.settings.toggle_full_screen()

print("\nAfter changing settings via Alice:\n")

# Show settings again
p1.show_settings()
p2.show_settings()
