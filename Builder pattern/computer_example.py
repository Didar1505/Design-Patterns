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
    def __init__(self):
        self.reset()

    def reset(self):
        self._computer = Computer()

    def set_motherboard(self, param):
        self._computer.motherboard = param
        return self

    def set_cpu(self, param):
        self._computer.cpu = param
        return self

    def set_ram(self,param):
        self._computer.ram = param
        return self


    def set_storage(self, param):
        self._computer.storage = param
        return self

    def set_gpu(self, param):
        self._computer.gpu = param
        return self
    
    def get_computer(self):
        temp = self._computer
        self.reset()
        return temp
    

class ComputerDirector:
    def __init__(self, builder:ComputerBuilder):
        self.builder = builder

    def build_office_pc(self):
        self.builder.set_motherboard("ASUS ATX 1050")
        self.builder.set_cpu('Intel core i5 9gen')
        self.builder.set_ram('8gb')
        self.builder.set_storage("SSD 518gb")
        

    def build_gaming_pc(self):
        self.builder.set_motherboard("ASUS ROG ATX 1070")
        self.builder.set_cpu('Intel core i9 14gen')
        self.builder.set_ram('64gb ram')
        self.builder.set_gpu("Nvidia RTX 5080 Super Ti")
        self.builder.set_storage('2TB SSD & 4TB HDD')


builder = ComputerBuilder()
director = ComputerDirector(builder)
director.build_gaming_pc()
computer = builder.get_computer()
print(computer)