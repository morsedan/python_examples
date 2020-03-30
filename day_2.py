class Animal:
    """A simple example class"""
    def __init(name, hunger, diet):
        self.name = name
        self.hunger = hunger
        self.diet = diet

    def __str__(self):
        return ""

    def __repr__(self):
        return ""

    def eat(self, food):
        if food > 0 and hunger < 25:
            hunger += food