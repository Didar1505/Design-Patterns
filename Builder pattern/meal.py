from abc import ABC, abstractmethod

class Meal:
    def __init__(self):
        self.main = None
        self.side = None
        self.drink = None
        self.dessert = None

    def __str__(self):
        group = ['main', 'side', 'drink', 'dessert']
        group = zip(group, [self.main, self.side, self.drink, self.dessert])
        group = list(group)
        ready  = map(lambda item: item[1] if item[1] else "No " + item[0], group)
        return f"Meal includes: \n\
{'\n'.join(ready)}"

class MealBuilder(ABC):

    @abstractmethod
    def set_main(self, main):
        pass

    @abstractmethod
    def add_side(self,side):
        pass

    @abstractmethod
    def add_drink(self, drink):
        pass
    
    @abstractmethod
    def add_desert(self, desert):
        pass
    
    @abstractmethod
    def get_meal(self):
        pass

class ConcreteMealBuilder(MealBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._meal = Meal()

    def set_main(self, main):
        self._meal.main = main
        return self

    def add_side(self, side):
        self._meal.side = side
        return self
    
    def add_desert(self, desert):
        self._meal.dessert = desert
        return self
    
    def add_drink(self, drink):
        self._meal.dring = drink
        return self

    def get_meal(self):
        temp = self._meal

        self.reset()

        return temp 
    

class Director:
    def __init__(self, builder:ConcreteMealBuilder):
        self._builder = builder

    def kids_pack(self):
        self._builder \
        .set_main("Small Burger") \
        .add_side("Small potato free") \
        .add_desert("Apple pie") \
        .add_drink("Apple juice")
        
    def adults_pack(self):
        self._builder \
        .set_main("Big double burger") \
        .add_side("Big potato free") \
        .add_desert("Cacao Cake") \
        .add_drink("Coca Cola") 
        

# my_meal = ConcreteMealBuilder()
# my_meal.set_main("Maestor Burger") \
# .add_desert("Apple pie") \
# .add_drink("Coca Cola") \
# .add_side('Cheese cake') \

builder = ConcreteMealBuilder()
director = Director(builder)
director.adults_pack()
result = builder.get_meal()
print(result)