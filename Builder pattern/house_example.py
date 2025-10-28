class House:
    def __init__(self, walls, roof, doors, windows, pool):
        self.walls = walls
        self.roof = roof
        self.doors = doors
        self.windows = windows
        self.pool = pool

    def add_part(self, part):
        self.parts.append(part)

    def __str__(self):
        parts = [self.walls, self.roof, self.doors, self.windows, self.pool]
        s = 'Дом состоит из: \n'
        for value in parts:
            if value:
                s += str(value) + "\n"
        return s

myhouse = House("Деревянные стена", 'Деревянный потолок', 'Простой дверь', "4 окна", False)
print(myhouse)