from typing import Any


class Dish():
    def __init__(self) -> None:
        self.ingredients = []
        self.instructions = ''
        self.price = 0

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def set_instructions(self, instructions):
        self.instructions = instructions
        
    def set_price(self, price):
        self.price = price