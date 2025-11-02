class Logger:
    _instance = None

    def __new__(cls):
        # TODO
        pass

    def __init__(self):
        self.messages = []

    def log(self, msg):
        pass


# Test
l1 = Logger()
l2 = Logger()

l1.log("Hello")
l2.log("World")

print(l1.messages) 
print(l2.messages)
