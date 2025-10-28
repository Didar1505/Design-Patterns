class Pizza:
    def __init__(self, size, cheese, pepperoni, mushrooms, onions, peppers, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.peppers = peppers
        self.bacon = bacon

    def __str__(self):
        parts = [self.size, "pizza with:"]
        if self.cheese: parts.append("cheese")
        if self.pepperoni: parts.append("pepperoni")
        if self.mushrooms: parts.append("mushrooms")
        if self.onions: parts.append("onions")
        if self.peppers: parts.append("peppers")
        if self.bacon: parts.append("bacon")
        return " ".join(parts)

my_pizza = Pizza("Large", True, True, False, True, False, False)
print(my_pizza)