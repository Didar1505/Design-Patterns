class Cache:
    _instance = None

    def __new__(cls):
        # TODO: implement singleton behavior
        pass

    def __init__(self):
        # Internal storage dictionary
        self._store = {}

    def set(self, key, value):
        # TODO: store value under key
        pass

    def get(self, key, default=None):
        # TODO: return stored value or default
        pass

    def delete(self, key):
        # TODO: remove item if it exists
        pass

    def clear(self):
        # TODO: wipe the whole cache
        pass


# --- Test Code ---
cache1 = Cache()
cache2 = Cache()

print("Same instance?", cache1 is cache2)  # should be True

cache1.set("user", "Alice")
print(cache2.get("user"))  # should print "Alice"
