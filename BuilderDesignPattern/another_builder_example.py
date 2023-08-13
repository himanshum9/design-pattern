## Wrong way to do this


class ComplexPizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False, extra_ingredients=[]):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.extra_ingredients = extra_ingredients

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.mushrooms:
            toppings.append("mushrooms")
        toppings.extend(self.extra_ingredients)
        return f"A {self.size} pizza with {', '.join(toppings)}."

# Client code
pizza = ComplexPizza("large", cheese=True, pepperoni=True, extra_ingredients=["olives", "spinach"])
print(pizza)


## Right way to do this


class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.mushrooms:
            toppings.append("mushrooms")
        return f"A {self.size} pizza with {', '.join(toppings)}."

class PizzaBuilder:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms)

# Client code
builder = PizzaBuilder("large")
pizza = builder.add_cheese().add_pepperoni().add_mushrooms().build()
print(pizza)
