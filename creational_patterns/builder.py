from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple

PizzaBase = namedtuple("PizzaBase", ["PizzaDoughDepth", "PizzaDoughType"])


class PizzaDoughDepth(Enum):
    THIN = auto()
    THICK = auto()


class PizzaDoughType(Enum):
    WHEAT = auto()
    CORN = auto()
    RYE = auto()


class PizzaSauceType(Enum):
    PESTO = auto()
    BBQ = auto()
    TOMATO = auto()


class PizzaTopLevelType(Enum):
    MOZZARELLA = auto()
    SALAMI = auto()
    BACON = auto()
    MUSHROOMS = auto()
    SHRIMPS = auto()


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        self.cooking_time_minute = None

    def __str__(self):
        info = \
            f"Pizza name: {self.name}\n" \
            f"Dough type: {self.dough.PizzaDoughDepth.name} & {self.dough.PizzaDoughType.name}\n" \
            f"Sauce type: {self.sauce}\n" \
            f"Topping: {[item.name for item in self.topping]}\n" \
            f"Cooking time: {self.cooking_time_minute} minutes"
        return info


class Builder(ABC):

    @abstractmethod
    def prepare_dough(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_topping(self):
        pass

    @abstractmethod
    def get_pizza(self):
        pass


class MargaritaPizzaBuilder(Builder):

    def __init__(self):
        self.pizza = Pizza("Margarita")
        self.pizza.cooking_time = 15

    def prepare_dough(self):
        self.pizza.dough = PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT)

    def add_sauce(self):
        self.pizza.sauce = PizzaSauceType.TOMATO

    def add_topping(self):
        self.pizza.topping.extend(
            [
                item for item in (PizzaTopLevelType.MOZZARELLA,
                                  PizzaTopLevelType.MOZZARELLA,
                                  PizzaTopLevelType.BACON)
            ]
        )

    def get_pizza(self):
        return self.pizza


class SalamiPizzaBuilder(Builder):

    def __init__(self):
        self.pizza = Pizza("Salami")
        self.pizza.cooking_time = 10

    def prepare_dough(self):
        self.pizza.dough = PizzaBase(PizzaDoughDepth.THIN, PizzaDoughType.RYE)

    def add_sauce(self):
        self.pizza.sauce = PizzaSauceType.BBQ

    def add_topping(self):
        self.pizza.topping.extend(
            [
                item for item in (PizzaTopLevelType.MOZZARELLA,
                                  PizzaTopLevelType.SALAMI)
            ]
        )

    def get_pizza(self):
        return self.pizza


class Director:

    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def make_pizza(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_topping()


if __name__ == "__main__":
    director = Director()

    for item in (MargaritaPizzaBuilder, SalamiPizzaBuilder):
        builder = item()
        director.set_builder(builder)
        director.make_pizza()
        pizza = builder.get_pizza()
        print(pizza)
        print("=" * 50)





