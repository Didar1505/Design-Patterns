""""Создайте строителя PizzaBuilder для класса Pizza"""
""""Дополнительно создайте директора DirectorBuilder который умеет готовить рецепты пицы"""

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.peppers = None
        self.bacon = None

    def __str__(self):
        parts = [self.size, "pizza with:"]
        if self.cheese: parts.append("cheese")
        if self.pepperoni: parts.append("pepperoni")
        if self.mushrooms: parts.append("mushrooms")
        if self.onions: parts.append("onions")
        if self.peppers: parts.append("peppers")
        if self.bacon: parts.append("bacon")
        return " ".join(parts)
    
class PizzaBuilder:
    pass

class BuilderDirector:
    pass