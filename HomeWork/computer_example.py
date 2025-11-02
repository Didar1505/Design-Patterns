""""Создайте строителя ComputerBuilder, который умеет строить части компьютера
Задача из классной работы. Далее создайте директора ComputerDirector который умеет
создать офисный и игровой компьютер с разными характеристиками.
"""

class Computer:
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
    
class ComputerBuilder:
    pass

class ComputerDirector:
    pass


