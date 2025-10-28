from abc import ABC, abstractmethod

class House:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def __str__(self):
        return str(self.parts)
    
class IHouseBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_pool(self):
        pass

    @abstractmethod
    def get_house(self):
        pass

class WoodenHouseBuilder(IHouseBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._house = House()

    def build_doors(self):
        self._house.add_part('Резная деревянная дверь')
        return self
    
    def build_pool(self):
        self._house.add_part('Бассейн с деревянным настилом')
        return self
    
    def build_roof(self):
        self._house.add_part('Деревянная крыша с черепицей')
        return self

    def build_walls(self):
        self._house.add_part('Деревянные стены')
        return self

    def build_windows(self):
        self._house.add_part('Деревянные окна со ставнями')
        return self

    def get_house(self):
        temp = self._house
        self.reset()
        return temp
    
class BrickHouseBuilder(IHouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()
    
    
    def build_walls(self):
        self._house.add_part('Кирпичные стены')
        return self

    def build_roof(self):
        self._house.add_part('Металлическая крыша')
        return self

    def build_doors(self):
        self._house.add_part('Стальная дверь')
        return self
    
    def build_windows(self):
        self._house.add_part('Пластиковые окна')
        return self
    
    def build_pool(self):
        print('Кирпичный строитель не строит бассейны.')
        return super().build_pool()
    
    def get_house(self):
        temp = self._house
        self.reset()
        return temp
    
class ConstructionDirector:
    def __init__(self, builder:IHouseBuilder):
        self._builder = builder
    
    def set_builder(self, builder:IHouseBuilder):
        self._builder = builder

    def build_simple_house(self):
        self._builder.build_walls()
        self._builder.build_doors()
        self._builder.build_windows()
        self._builder.build_roof()

    def build_luxury_house(self):
        self._builder.build_walls()
        self._builder.build_doors()
        self._builder.build_windows()
        self._builder.build_roof()
        self._builder.build_pool()
    

wooden = WoodenHouseBuilder()
brick = BrickHouseBuilder()
director = ConstructionDirector(brick)
director.build_luxury_house()
my_house = brick.get_house()
print(my_house)