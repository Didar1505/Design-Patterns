class Counter:
    _instance = None

    def __new__(cls):
        # TODO: реализовать логику singleton
        pass

    def __init__(self):
        self.value = 0

    def increment(self):
        # TODO: Увеличить значение счетчика (counter) на + 1
        pass


# Test
c1 = Counter()
c2 = Counter()

c1.increment()
c2.increment()

print(c1.value)  # должен быть 2
print(c2.value)  # должен быть 2