from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def deliver(self,package):
        pass

class Truck(Transport):
    def deliver(self, package):
        print(f"Доставляем '{package}' по земле на ГРУЗОВИКЕ.")

class Ship(Transport):
    def deliver(self, package):
        print(f"Доставляем '{package}' по морю на КОРАБЛЕ.")

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass
    
    def plan_delivery(self, package):
        print("Logistics: Планирую доставку...")
        transport = self.create_transport()
        transport.deliver(package)

class RoadLogistics(Logistics):
    def create_transport(self):
        print("RoadLogistics: Создаю грузовик.")
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        print("SeaLogistics: Создаю корабль.")
        return Ship()
    
def client_code(logistics_creator:Logistics, package):
    logistics_creator.plan_delivery(package)

print("--- Пример с Фабричным Методом ---")

print("\nСценарий: Нужна доставка по земле.")
road_logistics = RoadLogistics()
client_code(road_logistics, "Коробка с электроникой")

print("\nСценарий: Нужна доставка по морю.")
sea_logistics = SeaLogistics()
client_code(sea_logistics, "Большой контейнер")