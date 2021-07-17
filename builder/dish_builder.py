from interfaces import IDishBuilder
from dish import Dish

class DishBuilder(IDishBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._dish = Dish()

    @property
    def dish(self):
        dish = self._dish
        self.reset()
        return dish