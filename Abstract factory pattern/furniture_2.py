from abc import ABC, abstractmethod

class IChair(ABC):
    @abstractmethod
    def sit_on(self):
        pass
class ISofa(ABC):
    @abstractmethod
    def relax_on(self):
        pass
class ITable(ABC):
    @abstractmethod
    def place_items(self):
        pass

class ArtDecoChair(IChair):
    def sit_on(self):
        print('Сижу на стильном кресле Ар-деко.')
class ArtDecoSofa(ISofa):
    def relax_on(self):
        print('Отдыхаю на роскошном диване Ар-деко.')
class ArtDecoTable(ITable):
    def place_items(self):
        print('Кладу напиток на столик Ар-деко с глянцевой поверхностью.')

class VictorianChair(IChair):
    def sit_on(self):
        print("Приседаю на элегантное кресло Викторианского стиля.")
class VictorianSofa(ISofa):
    def relax_on(self):
        print('Расслабляюсь на богато украшенном Викторианском диване.')
class VictorianTable(ITable):
    def place_items(self):
        print("Кладу кружево на резной Викторианский столик.")

class ModernChair(IChair):
    def sit_on(self):
        print("Ощущаю минимализм на современном кресле.")
class ModernSofa(ISofa):
    def relax_on(self):
        print("Наслаждаюсь простыми линиями на диване Модерн.")
class ModernTable(ITable):
    def place_items(self):
        print("Кладу телефон на гладкий столик Модерн.")

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> IChair:
        pass
    @abstractmethod
    def create_sofa(self) -> ISofa:
        pass
    @abstractmethod
    def create_table(self) -> ITable:
        pass

class ArtDecoFactory(FurnitureFactory):
    def create_chair(self):
        return ArtDecoChair()
    def create_sofa(self):
        return ArtDecoSofa()
    def create_table(self):
        return ArtDecoTable()
    
class VictorianFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()
    def create_sofa(self):
        return VictorianSofa()
    def create_table(self):
        return VictorianTable()
    
class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    def create_sofa(self):
        return ModernSofa()
    def create_table(self):
        return ModernTable()


def furnish_room(factory:FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    table = factory.create_table()

    chair.sit_on()
    sofa.relax_on()
    table.place_items()
   

all_types = [ArtDecoFactory(), VictorianFactory(), ModernFactory()]

for each in all_types:
    furnish_room(each)
    print("--")