class Computer:
    """The complex object we want to build"""
    def __init__(self):
        self.motherboard = None
        self.cpu = None
        self.ram = 0
        self.storage = 0
        self.gpu = None
        

    def __str__(self):
        return (
            f"Computer Specs:\n"
            f"  Mother Board: {self.motherboard}\n"
            f"  CPU: {self.cpu}\n"
            f"  RAM: {self.ram}GB\n"
            f"  Storage: {self.storage}GB SSD\n"
            f"  GPU: {self.gpu}"
        )